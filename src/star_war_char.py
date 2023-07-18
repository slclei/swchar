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
                # In case of empty star ship, set ships to be default
                if ships_urls==[]:
                    ships=[['Not Provided']*3]
                else:
                    # Get each star ship information
                    ships=[]
                    for ships_url in ships_urls:
                        ships.append(self.get_starship(ships_url))

                # Get home planet for this character, url to home planet
                home_planet_url=result['homeworld']
                # In case of empty hom planet, set home to be default
                if home_planet_url=="":
                    home=[['Not Provided']*3]
                else:
                    # Get home planet information
                    home=self.get_home_planet(home_planet_url)

                # Get species, list with urls to species
                species_urls=result['species']
                # In case of empty species, set species to be default
                if species_urls==[]:
                    species=[['Not provided']*3]
                else:
                    # Get each species informaiton
                    species=[]
                    for species_url in species_urls:
                        species.append(self.get_species(species_url))

                # Add this character to chars list
                self.chars[name]=[ships,[home],species]
                self.name.append(name)

            # sort name list
            self.name.sort()

        else:
            # Print an error message
            self.error="Error:" + response.status_code

    # Get starship information
    # Return: [starship name, cargo capacity, starship class]
    def get_starship(self,url):
        # Return results. Default value is 'not provided'. 
        res=['Not Provided']*3

        # Get response from url
        response = requests.get(url)
        # Get information in dictionary
        results=json.loads(response.content.decode())
        
        # Update value only if the value is provided
        if results['name']!='':
            res[0]=results['name']
        if results['cargo_capacity']!='':
            res[1]=results['cargo_capacity']
        if results['starship_class']!='':
            res[2]=results['starship_class']

        return res


    # Get home planet information
    # Return: [planet name, population, climate]
    def get_home_planet(self,url):
        # Return results. Default value is 'not provided'. 
        res=['Not Provided']*3
        
        # Get response from url
        response = requests.get(url)
        # Get information in dictionary
        results=json.loads(response.content.decode())

        # Update value only if the value is provided
        if results['name']!='':
            res[0]=results['name']
        if results['population']!='':
            res[1]=results['population']
        if results['climate']!='':
            res[2]=results['climate']

        # Return results
        return res

    # Get species information
    # Return: [Name, language, average lifespan]
    def get_species(self,url):
        # Return results. Default value is 'not provided'. 
        res=['Not Provided']*3
        
        # Get response from url
        response = requests.get(url)
        # Get information in dictionary
        results=json.loads(response.content.decode())

        # Update value only if the value is provided
        if results['name']!='':
            res[0]=results['name']
        if results['language']!='':
            res[1]=results['language']
        if results['average_lifespan']!='':
            res[2]=results['average_lifespan']

        # Return results
        return res