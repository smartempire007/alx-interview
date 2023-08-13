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

/**
 * This script retrieves information about characters from a Star
 * Wars movie using the Star Wars API.
 * It takes a movie ID as a command-line argument and fetches the
 * corresponding movie data from the API.
 * The script then extracts the URLs of each character appearing
 * in the movie and makes additional requests to retrieve their details.
 * Finally, it prints the name of each character in the order of their
 * appearance in the movie.
 *
 * Dependencies:
 * - request: npm package for making HTTP requests
 *
 * Usage: node script.js <movieID>
 * Example: node script.js 3
 */

const request = require('request');

// Get the movie ID from the command-line argument
const movieId = process.argv[2] + '/';
const filmURL = 'https://swapi-api.hbtn.io/api/films/';

// Make an API request to fetch movie data
request(filmURL + movieId, async (err, res, body) => {
  if (err) return console.error(err);

  // Extract URLs of each character in the movie as a list object
  const charURLList = JSON.parse(body).characters;

  // Use the URL list to make new requests for character details
  // Await ensures that requests are processed in sequential order
  for (const charURL of charURLList) {
    await new Promise((resolve, reject) => {
      request(charURL, (err, res, body) => {
        if (err) return console.error(err);

        // Extract the character name from the response body and print it
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});