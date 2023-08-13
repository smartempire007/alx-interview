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

const request = require('request-promise');

/**
 * Fetches and prints characters of the specified Star Wars movie.
 */
const fetchData = async () => {
  try {
    const movieId = process.argv[2] + '/';
    const filmURL = 'https://swapi-api.hbtn.io/api/films/';

    // Fetch movie data
    const filmData = await request(filmURL + movieId);
    const filmJson = JSON.parse(filmData);

    const characters = filmJson.characters;

    // Fetch character data using promises
    const characterPromises = characters.map(
        character => request(character));
    const characterResponses = await Promise.all(
        characterPromises);
    const characterData = characterResponses.map(
        response => JSON.parse(response));

    // Print character names
    for (const character of characterData) {
      console.log(character.name);
    }
  } catch (error) {
    console.log(error);
  }
};

// Invoke the fetchData function to start the process
fetchData();