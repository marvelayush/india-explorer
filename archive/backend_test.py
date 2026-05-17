import requests
import sys
import json
from datetime import datetime

class IndiaExplorerAPITester:
    def __init__(self, base_url="https://india-explorer-43.preview.emergentagent.com"):
        self.base_url = base_url
        self.tests_run = 0
        self.tests_passed = 0
        self.failed_tests = []

    def run_test(self, name, method, endpoint, expected_status, expected_count=None, data=None):
        """Run a single API test"""
        url = f"{self.base_url}/api/{endpoint}"
        headers = {'Content-Type': 'application/json'}

        self.tests_run += 1
        print(f"\n🔍 Testing {name}...")
        print(f"   URL: {url}")
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers, timeout=10)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=headers, timeout=10)

            success = response.status_code == expected_status
            
            if success:
                try:
                    response_data = response.json()
                    if expected_count is not None:
                        if isinstance(response_data, list):
                            actual_count = len(response_data)
                        elif isinstance(response_data, dict):
                            # For search results or state with places
                            if 'states' in response_data and 'places' in response_data:
                                actual_count = len(response_data['states']) + len(response_data['places'])
                            elif 'places' in response_data:
                                actual_count = len(response_data['places'])
                            else:
                                actual_count = 1
                        else:
                            actual_count = 1
                            
                        if actual_count >= expected_count:
                            print(f"✅ Passed - Status: {response.status_code}, Count: {actual_count}")
                            self.tests_passed += 1
                        else:
                            print(f"❌ Failed - Expected at least {expected_count} items, got {actual_count}")
                            self.failed_tests.append(f"{name}: Expected count >= {expected_count}, got {actual_count}")
                            success = False
                    else:
                        print(f"✅ Passed - Status: {response.status_code}")
                        self.tests_passed += 1
                except json.JSONDecodeError:
                    print(f"❌ Failed - Invalid JSON response")
                    self.failed_tests.append(f"{name}: Invalid JSON response")
                    success = False
            else:
                print(f"❌ Failed - Expected {expected_status}, got {response.status_code}")
                if response.text:
                    print(f"   Response: {response.text[:200]}")
                self.failed_tests.append(f"{name}: Expected {expected_status}, got {response.status_code}")

            return success, response.json() if success else {}

        except requests.exceptions.RequestException as e:
            print(f"❌ Failed - Network Error: {str(e)}")
            self.failed_tests.append(f"{name}: Network error - {str(e)}")
            return False, {}
        except Exception as e:
            print(f"❌ Failed - Error: {str(e)}")
            self.failed_tests.append(f"{name}: Error - {str(e)}")
            return False, {}

    def test_root_endpoint(self):
        """Test API root endpoint"""
        return self.run_test("API Root", "GET", "", 200)

    def test_get_all_states(self):
        """Test getting all states - should return 36 states/UTs"""
        return self.run_test("Get All States", "GET", "states", 200, expected_count=36)

    def test_get_specific_state(self, state_slug="rajasthan"):
        """Test getting a specific state with places"""
        success, response = self.run_test(f"Get State: {state_slug}", "GET", f"states/{state_slug}", 200)
        if success and 'state' in response and 'places' in response:
            print(f"   State: {response['state']['name']}")
            print(f"   Places count: {len(response['places'])}")
            if len(response['places']) >= 3:
                print(f"✅ State has adequate places data")
                return True, response
            else:
                print(f"⚠️  Warning: State has only {len(response['places'])} places")
                return True, response
        return success, response

    def test_get_specific_place(self, place_slug="taj-mahal"):
        """Test getting a specific place with related places"""
        success, response = self.run_test(f"Get Place: {place_slug}", "GET", f"places/{place_slug}", 200)
        if success and 'place' in response:
            print(f"   Place: {response['place']['name']}")
            print(f"   Related places: {len(response.get('related_places', []))}")
            return True, response
        return success, response

    def test_search_functionality(self):
        """Test search with various queries"""
        test_queries = [
            ("Taj Mahal", "places"),
            ("Rajasthan", "states"),
            ("UNESCO", "places"),
            ("temple", "places")
        ]
        
        all_passed = True
        for query, expected_type in test_queries:
            success, response = self.run_test(f"Search: {query}", "GET", f"search?q={query}", 200)
            if success:
                if expected_type == "places" and len(response.get('places', [])) > 0:
                    print(f"   Found {len(response['places'])} places")
                elif expected_type == "states" and len(response.get('states', [])) > 0:
                    print(f"   Found {len(response['states'])} states")
                else:
                    print(f"   No {expected_type} found for query: {query}")
            else:
                all_passed = False
        
        return all_passed

    def test_categories_endpoint(self):
        """Test getting categories"""
        return self.run_test("Get Categories", "GET", "categories", 200, expected_count=5)

    def test_invalid_endpoints(self):
        """Test error handling for invalid endpoints"""
        invalid_tests = [
            ("Invalid State", "GET", "states/invalid-state", 404),
            ("Invalid Place", "GET", "places/invalid-place", 404),
        ]
        
        all_passed = True
        for name, method, endpoint, expected_status in invalid_tests:
            success, _ = self.run_test(name, method, endpoint, expected_status)
            if not success:
                all_passed = False
        
        return all_passed

def main():
    print("🚀 Starting India Explorer API Tests")
    print("=" * 50)
    
    tester = IndiaExplorerAPITester()
    
    # Test sequence
    tests = [
        ("API Root", tester.test_root_endpoint),
        ("All States", tester.test_get_all_states),
        ("Specific State (Rajasthan)", lambda: tester.test_get_specific_state("rajasthan")),
        ("Specific Place (Taj Mahal)", lambda: tester.test_get_specific_place("taj-mahal")),
        ("Search Functionality", tester.test_search_functionality),
        ("Categories", tester.test_categories_endpoint),
        ("Error Handling", tester.test_invalid_endpoints),
    ]
    
    for test_name, test_func in tests:
        print(f"\n📋 Running {test_name} tests...")
        try:
            test_func()
        except Exception as e:
            print(f"❌ Test suite {test_name} failed with error: {str(e)}")
            tester.failed_tests.append(f"{test_name}: Exception - {str(e)}")
    
    # Print summary
    print("\n" + "=" * 50)
    print(f"📊 Test Results Summary")
    print(f"Tests Run: {tester.tests_run}")
    print(f"Tests Passed: {tester.tests_passed}")
    print(f"Tests Failed: {tester.tests_run - tester.tests_passed}")
    print(f"Success Rate: {(tester.tests_passed/tester.tests_run*100):.1f}%" if tester.tests_run > 0 else "0%")
    
    if tester.failed_tests:
        print(f"\n❌ Failed Tests:")
        for i, failure in enumerate(tester.failed_tests, 1):
            print(f"   {i}. {failure}")
    else:
        print(f"\n✅ All tests passed!")
    
    return 0 if tester.tests_passed == tester.tests_run else 1

if __name__ == "__main__":
    sys.exit(main())