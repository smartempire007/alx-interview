#!/usr/bin/node

/**
 * Prints all characters of a Star Wars movie.
 * The first positional argument passed is the Movie ID,
 * which corresponds to a specific Star Wars movie.
 * Displays one character name per line in the same order
 * as the "characters" list in the /films/ endpoint.
 * Uses the Star Wars API (https://swapi-api.hbtn.io)
 * to fetch movie and character data.
 * Utilizes the request-promise module for making HTTP requests.
 */

const request = require('request');

const movieId = process.argv[2];
const movieEndpoint = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

// Function to send requests for each character URL
function sendRequest(characterList, index) {
  // Base case: check if we have reached the end of the character list
  if (characterList.length === index) {
    return;
  }

  // Make an HTTP request for the character URL
  request(characterList[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      // Print the character's name from the response body
      console.log(JSON.parse(body).name);

      // Recursively call sendRequest to make the next request
      sendRequest(characterList, index + 1);
    }
  });
}

// Make an HTTP request to get movie data
request(movieEndpoint, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    // Parse the response body to get the list of characters
    const characterList = JSON.parse(body).characters;

    // Start sending requests for each character URL
    sendRequest(characterList, 0);
  }
});
