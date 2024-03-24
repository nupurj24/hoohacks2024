# Restaurants that are known to have eco-friendly containers and ultensils based on our research

class EcoRestaurants:
    def __init__(self):
        self.ecorestaurants = ['CAVA', 'Chipotle', 'Panera', 'Noodles and Company', 'Burger King']
    
    def getEcorestaurantsJSON(self):
        json_ecorestaurants = []
        for restaurant in self.ecorestaurants:
            json_ecorestaurant = {
                'name': restaurant
            }
            json_ecorestaurants.append(json_ecorestaurant)
        return json_ecorestaurants