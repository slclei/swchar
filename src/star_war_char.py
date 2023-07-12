import requests
import json

class Star_war_char:
    def __init__(self):
        # Define the base url fro swapi
        self.base_url = "http://swapi.dev/api/"
        # Define a dictionary to store all characters, with the name as key,an array with startships, home planet, and species as value
        self.chars={} 
        self.name=[]
        self.error=""

    # Get characters' information with the name
    def get_chars(self,name):
        # Define the url to get this character
        url=self.base_url+"/people/?search="+name

        # Get response from url
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Store results
            results=json.loads(response.content.decode())['results']
            
            # Loop in results to get information from each character
            for result in results:
                # Get character name, string
                name=result['name']

                # Get star ships for this character, list with urls to star shpis
                ships_urls=result['starships']
                # Get each star ship information
                ships=[]
                for ships_url in ships_urls:
                    ships.append(self.get_starship(ships_url))

                # Get home planet for this character, url to home planet
                home_planet_url=result['homeworld']
                # Get home planet information
                home=self.get_home_planet(home_planet_url)

                # Get species, list with urls to species
                species_urls=result['species']
                # Get each species informaiton
                species=[]
                for species_url in species_urls:
                    species.append(self.get_species(species_url))

                # Add this character to chars list
                self.chars[name]=[ships,home,species]
                self.name.append(name)

            # sort name list
            self.name.sort()
            print(self.name)

        else:
            # Print an error message
            self.error="Error:" + response.status_code

    # Get starship information
    # Return: [starship name, cargo capacity, starship class]
    def get_starship(self,url):
        # Get response from url
        response = requests.get(url)
        # Get information in dictionary
        results=json.loads(response.content.decode())
        # Return results
        return [results['name'],results['cargo_capacity'],results['starship_class']]


    # Get home planet information
    # Return: [planet name, population, climate]
    def get_home_planet(self,url):
        # Get response from url
        response = requests.get(url)
        # Get information in dictionary
        results=json.loads(response.content.decode())
        # Return results
        return [results['name'],results['population'],results['climate']]

    # Get species information
    # Return: [Name, language, average lifespan]
    def get_species(self,url):
        # Get response from url
        response = requests.get(url)
        # Get information in dictionary
        results=json.loads(response.content.decode())
        # Return results
        return [results['name'],results['language'],results['average_lifespan']]