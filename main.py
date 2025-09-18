
from structures.hash_map import HashMap
from structures.graph import Graph
from structures.avl_tree import AVLTree
from structures.trie import Trie
from structures.min_heap import MinHeap
from structures.max_heap import MaxHeap
from structures.bst import BST
from structures.disjoint_set import DisjointSet
from structures.max_flow import MaxFlow
import copy

# Main disaster response system# Main disaster response system
class DisasterResponseSystem:
    def __init__(self):
        self.graph = Graph()
        self.resource_graph = Graph()
        self.disaster_types = AVLTree()
        self.locations = Trie()
        self.emergency_heap = MaxHeap()
        self.historical_responses = BST()
        self.MaxFlow = MaxFlow()
        self.historical_root = None

        self.emergency_contacts = HashMap()  # Stores emergency contacts for each city
        self.resource_inventory = HashMap()  # Stores available resources in each city


    def add_city_and_route(self):
        city1 = input("Enter the first city: ")
        city2 = input("Enter the second city: ")
        distance = int(input("Enter distance between cities: "))
        self.graph.add_route(city1, city2, distance)
        self.add_location(city1)
        self.add_location(city2)
        print(f"Route added between {city1} and {city2}.")

    def insert_disaster_type_with_severity(self):
        disaster_type = input("Enter disaster type: ")
        severity = int(input("Enter severity (1-10): "))
        self.disaster_types.root = self.disaster_types.insert(self.disaster_types.root, disaster_type, severity)
        print(f"Disaster type {disaster_type} with severity {severity} inserted.")


    def all_emergencies(self):
        self.emergency_heap.display()

    def search_location(self):
        location = input("Enter location to search: ")
        if self.locations.search(location):
            print(f"Location {location} found.")
        else:
            print(f"Location {location} not found.")

    def add_location(self,location):
        
        self.locations.insert(location)
        print(f"Location '{location}' added to the system.")

    def add_emergency_with_urgency(self):
        emergency = input("Enter emergency description: ")
        urgency = int(input("Enter urgency (1-10): "))
        self.emergency_heap.push((urgency, emergency))
        print(f"Emergency '{emergency}' added with urgency {urgency}.")

    def insert_historical_response_data(self):
        key = input("Enter historical response key: ")
        data = input("Enter response data: ")
        self.historical_root = self.historical_responses.insert(self.historical_root, key, data)
        print("Historical response data inserted.")

    def find_shortest_path_between_cities(self):
        start = input("Enter start city: ")
        end = input("Enter end city: ")
        distance = self.graph.shortest_path(start, end)
        if distance == -1:
            print(f"No path found between {start} and {end}.")
        else:
            print(f"The shortest path between {start} and {end} is {distance} units.")

    def display_top_priority_emergency(self):
        if not self.emergency_heap.is_empty():
            self.emergency_heap.top()
        else:
            print("No emergencies in the queue.")

    def search_historical_response(self):
        key = input("Enter historical response key to search: ")
        response = self.historical_responses.search(self.historical_root, key)
        if response:
            print(f"Response data for key '{key}': {response.data}.")
        else:
            print(f"No historical response found for key '{key}'.")

    def display_minimal_cost_travel(self):
        mst_edges = self.graph.prim_mst()
        
    def travel_cities(self):
        start = input("Enter city : ")
        self.graph.dfs(start,set())

    def display_disasters(self):

        self.disaster_types.inorder(self.disaster_types.root)
        print()

    def max_flow(self):
        src = input("Enter source : ")
        sink = input("Enter sink : ")
        
        # Create a deep copy of the original graph
        graph = copy.deepcopy(self.resource_graph.adj_list)

        print("Max Flow: ", self.MaxFlow.ford_fulkerson(src, sink, graph))


    def add_resource_route(self):
        """Add a resource connection between two cities"""
        city1 = input("Enter the first city: ")
        city2 = input("Enter the second city: ")
        resources = int(input("Enter resource amount available on this route: "))
        
        # Check if cities exist in the main graph
        if city1 not in self.graph.adj_list or city2 not in self.graph.adj_list:
            print("Error: Both cities must exist in the main network first.")
            return
            
        self.resource_graph.add_route(city1, city2, resources)
        print(f"Resource route added between {city1} and {city2} with {resources} units.")



    def minimal_resources(self):
        self.resource_graph.prim_mst()


    def add_emergency_contact(self):
        """Add emergency contact information for a city"""
        city = input("Enter city name: ")
        if city not in self.graph.adj_list:
            print("Error: City does not exist in the network.")
            return
        
        contacts = {
            "police": input("Enter police emergency number: "),
            "fire": input("Enter fire department number: "),
            "ambulance": input("Enter ambulance service number: "),
            "disaster_control": input("Enter disaster control room number: ")
        }
        self.emergency_contacts.add(city, contacts)
        print(f"Emergency contacts added for {city}")

    def get_emergency_contacts(self):
        """Retrieve emergency contacts for a city"""
        city = input("Enter city name: ")
        contacts = self.emergency_contacts.get(city)
        if contacts:
            print(f"\nEmergency Contacts for {city}:")
            for service, number in contacts.items():
                print(f"{service.title()}: {number}")
        else:
            print(f"No emergency contacts found for {city}")

    def update_resource_inventory(self):
        """Update resource inventory for a city"""
        city = input("Enter city name: ")
        if city not in self.graph.adj_list:
            print("Error: City does not exist in the network.")
            return
        
        resources = {
            "Food_quantity": int(input("Amount of food quantity : ")),
            "fire_trucks": int(input("Number of fire trucks: ")),
            "rescue_teams": int(input("Number of rescue teams : ")),
            "medical_supplies": int(input("Units of medical supplies : ")),
            "emergency_shelters": int(input("Number of emergency shelters : "))
        }
        self.resource_inventory.add(city, resources)
        print(f"Resource inventory updated for {city}")

    def check_resource_availability(self):
        """Check available resources in a city"""
        city = input("Enter city name: ")
        resources = self.resource_inventory.get(city)
        if resources:
            print(f"\nAvailable Resources in {city}:")
            for resource, quantity in resources.items():
                print(f"{resource.replace('_', ' ').title()}: {quantity}")
        else:
            print(f"No resource inventory found for {city}")

   



    def run(self):
        while True:
            print("\nDisaster Response System")
            print("1. Add City and Route")
            print("2. insert disaster with severity ")
            print("3. Search Location")
            print("4. Add Emergency with Urgency")
            print("5. Insert Historical Response Data")
            print("6. Find Shortest Path Between Cities")
            print("7. Display Top Priority Emergency")
            print("8. Display all emergencies")
            print("9. Search Historical Response")
            print("10. Minimal cost Travel")
            print("11. Travel Cities ")
            print("12. Max Flow between cities")
            print("13. display Disasters  ")
            print("14. Add resources ")
            print("15. minimal resources ")
            print("16. Add Emergency Contacts for City")
            print("17. View Emergency Contacts")
            print("18. Add/Update Resource Inventory")
            print("19. Check Resource Availability")
            print("0. Exit")

            choice = input("Select an option: ")
            if choice == "1":
                self.add_city_and_route()
            elif choice == "2":
                self.insert_disaster_type_with_severity()
            elif choice == "3":
                self.search_location()
            elif choice == "4":
                self.add_emergency_with_urgency()
            elif choice == "5":
                self.insert_historical_response_data()
            elif choice == "6":
                self.find_shortest_path_between_cities()
            elif choice == "7":
                self.display_top_priority_emergency()
            elif choice =="8":
                self.all_emergencies()
            elif choice == "9":
                self.search_historical_response()
            elif choice == "10":
                self.display_minimal_cost_travel()
            elif choice=="11":
                self.travel_cities()
            elif choice=="12":
                self.max_flow()
            elif choice=="13":
                self.display_disasters()
            elif choice=="14":
                self.add_resource_route()
            elif choice=="15":
                self.minimal_resources()
            elif choice == "16":
                self.add_emergency_contact()
            elif choice == "17":
                self.get_emergency_contacts()
            elif choice == "18":
                self.update_resource_inventory()
            elif choice == "19":
                self.check_resource_availability()
            elif choice == "0":
                print("Exiting the Disaster Response System.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    system = DisasterResponseSystem()
    system.run()
