Program Description

The Tino's Search engine is a program designed to retrive movie data from the API server "http://www.omdbapi.com/?i=tt3896198&apikey=" + "45764e23", based of input of a movie title from the user. This program will then send requests to the API server and the server will return movie data in JSON format which will be converted to a readable format by the program and displayed in a neat uniform manner and saved to a .txt file on the computer.

API's and REST API's

What is an API

An Application Programming Interface also known as an API is essentially a server that is used to retrive and send data through a code eg My search engine program above.

How to interact with an API through Python

To get information from an API in python the user needs to make a request to the API server. this is done by using the python libraries specifically the "requests" librabry. This library is not part of the python packages so you are required to install it before using this library by using "pip Intall requests". when you have installed the library you need to import it into your program to be able to use it by using "import requests"

How to use this API and handle the responses that it provides

To use the API can be done via many ways through a varaity of requets. In my program i used the "GET" request i only needed to retrive data from the API. When making a request to the API the response comes with a "response code" which just tells the user weather the request was successfull or not.

To make the "Get" request i used "request.get()" function which requires a single argument which is the API URL. response = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=" + "45764e23").

The "Get()" funtions returns a response object and to be able to receive the status code of my request i used the "response.status_code" function.

The information from the API is returned in JSON format. JSON as known as JavaScript Object Notation is a method is a method used to encode data structures that ensure that information is easily understood by the computers. The output received from the API looks like it contains a combination python dictionaries, lists etc.

REST API

A REST API is type of application for API's that uses HTTP requests to access and use the data from the server

This data can be used for a varaity of things for example to "GET, PUT, POST and, DELETE data types which usally refer to the reading, creating, and deleting of operations concerning resources.

How interaction takes place between the program and REST API

When using the REST API the server and program can onlt interract in one way. The program will send a request to server and then the server will return a response back to the program. All request and interaction have to intiated by the program as server are not able to send requsets to program.
