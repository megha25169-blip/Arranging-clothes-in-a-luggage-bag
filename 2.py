"""
Algorithm: Pack Clothes in a Luggage Bag
1. Define trip activities (sightseeing, hiking, formal dinner, etc.).
2. Assign clothes and accessories to each activity.
3. Pack items ensuring:
   - Heavy items at the bottom
   - Frequently used items on top
   - Delicate items protected by soft clothes
4. Provide a function to retrieve items by activity.
"""

class LuggageBag:
    def __init__(self):
        # Dictionary: activity -> list of items
        self.activities = {}

    def add_item(self, activity, item):
        if activity not in self.activities:
            self.activities[activity] = []
        self.activities[activity].append(item)

    def get_items(self, activity):
        return self.activities.get(activity, [])

# Example usage
bag = LuggageBag()
bag.add_item("Sightseeing", "Jeans")
bag.add_item("Hiking", "Sports Shoes")
bag.add_item("Formal Dinner", "Cocktail dress")

print("Items for Hiking:", bag.get_items("Hiking"))