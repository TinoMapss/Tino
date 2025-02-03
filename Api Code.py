import requests
import omdb #importing librabries

API_KEY = "45764e23" #API keys used to Access the API servers
omdb.set_default( 'apikey', '45764e23')


def print_heading(heading_text):
    heading_length = len(heading_text)
    underline = '=' * heading_length
    print(f"{heading_text}\n{underline}") #creates the heading
    
print_heading("WELCOME TO TINO'S MOVIE SEARCH DATA BASE")

try:
    response = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=" + "45764e23") #sends a request to the API

    if response.status_code == 200:# used to check the server connection status 
        print("Connected")

        while True:  #starts the loop
            start = input("\nPRESS 'E' THEN ENTER BUTTON TO SEARCH OR Press 'Q' THN ENTER BUTTON TO QUIT: ")

            if start.upper() == 'E':
                movie = input("\nEnter movie title: ") #prompt for user to enter movie title

                try:
                    result = omdb.title(movie) #checking weather if movie exists

                    if result != None:
                        print("\nSearch Results:")
                        print("Title:", result['title'])
                        print("Genre:", result['genre'])
                        print("Release Date:", result['released'])
                        print("Runtime:", result['runtime'])
                        print("Director:", result['director'])
                        print("Awards:", result['awards']) # movie data is displayed in this order
                        
                        save_file = input(" \nWOULD YOU LIKE TO SAVE THIS SEARCH? (Y/N): ") #prompt to ask user to save movie data
                        if save_file.upper() == 'Y':
                            with open('movie_info.txt', 'a') as file:  #movie data saving to .txt file
                                file.write("Title: " + result['title'] + "\n") #appeneding info to .txt file
                                file.write("Genre: " + result['genre'] + "\n")
                                file.write("Release Date: " + result['released'] + "\n")
                                file.write("Runtime: " + result['runtime'] + "\n")
                                file.write("Director: " + result['director'] + "\n")
                                file.write("Awards: " + result['awards'] + "\n")
                                file.write("........................................\n")
                                print("\nMOVIE INFO SAVE TO 'movie_info.txt'.") 
                    else:
                        print("      ")
                except Exception as e:
                    print("Sorry Mate can't find what you're looking for. :/") #can not find movie

            elif start.upper() == 'Q':
                print("\n\t\tTHANK YOU SEARCH AGAIN SOON ;)")
                break # ends the loop
            else:
                print("\tOIIIII, EITHER PRESS Q OR E!!!!") #runs when user does not input that is not Q or E
    else:
        print("\tOIIIII, EITHER PRESS Q OR E!!!!")
except Exception as e:
    print("Error 404: Failed to connect (×_×)") #runs when connection to server is not complete
