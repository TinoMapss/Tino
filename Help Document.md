How to use the program:

1. To use the programme the user to prompted to enter either 'E' or 'Q'. To run the Programme user should input 'E' and then press enter.

2. Then the user while be prompted to enter a movie title of their choice for example "Cars" and before pressing ENTER user should check the Spelling of Movie title before procceding.

3. The results of the movie will then be displayed.

4. The user will be asked if you would like save the search data via a (Y/N) prompt with 'Y' = Yes and 'N' = No.

5. Then programe will prompt the user if you would like to search for another movie or Exit the program via the pormpt "Oi, either press Q or E!!!!" with 'Q' = Quit and 'E' to search again.

6. If 'Q' is selected the program will close and the program will display 'THANK YOU SEARCH AGAIN SOON'.

7. If 'E' is selected please refer to step 2 and repeat the steps.

Possible errors:

The first error that could occur is failure to connect to the API server and the 'get' request is not completed. this would have been casued by the program having no connection to the internet therefore preventing it from receving any data.

The program will not run if the user does not enter 'E' into the prompt.

Another error that could occur is not displaying the movie data, this could be caused by 2 main reasons either the movie does not exist or that the spelling of thee movie is wrong and computer is not able to undertand it.

retrospective

Problems encounterd:

1. The output was hard to read = the final output was produced in JSON format when i used the Print(result) which made difficult to read

2. Importing the OMDB module

3. Setting the default API key = In the original code, the function call omdb.set_defult("Api", "45764e23") had a typo in the method name (set_defult instead of set_default), and the API key and parameter were not passed correctly.

4. Inputting the movie title = 4. In my first code i had put the input statement before the program checked the status code of the API response.

5. Crashing IF function = i first used the if function but it kept crashing because it was not able to catch any errors for example it would crash every time the movie searched did not exist or when the program failed to connect to the server.

6. Checking for an empty response = When the program checked for an empty response in my first code i used the Condition omdb.title(movie) to check for an empty resopnse but the omdb.title(movie) function would return "None" when there were no results found.

7. The programme was not user friendly

solutions:

1. Since the omdb.title() function returns a dictionary, so it needs to be printed separately. The variable result is used to store the movie details and printed out instead.
2. Had to import the OMDB module separalty
3. i was able to fix this by setting the defult API key using the variable API_KEY
4. In the updated code i moved the input statement inside the IF block to ask the user for movie after the connection is successful.
5. Changed the if to a Try Function to help capture the errors
6. I updated the conditions to check if the "result" is "none" instead
7. gave my roomate to try the program he critised the UI presentation, and ask for his thouhts yo make it more user friendly

Improvements:

1. The code do with more use of the "Def" function to reduce repetition and make the code shorter

lessons:

1. I learnt to incorperate the 'Try' function over the 'If' function because the 'try' function is able to handle errors better and also it doesnt crash when an error occurs.
2. The use of "with open('movie_info.txt', 'a')" add new information to a file quicker and faster than methods. becasue it automatically opens and close when you exit the code
3. Another lesson would regard how an API works and also how the server interacts with the programme
​
