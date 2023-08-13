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

// Import required modules
const request = require('request');

// Retrieve and validate the movieId from command line arguments
const movieId = process.argv[2];
if (process.argv.length !== 3 || !Number(movieId)) {
  process.exit(1);
}

// Define the URL for fetching movie data based on the movieId
const filmUri = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

/**
 * Fetches and prints the name of a character from their API URI
 * @param {string} characterUri - The URI of the character endpoint
 * @returns {Promise<string>} - A promise that resolves with the character's name
 */
const printCharacterName = (characterUri) => {
  return new Promise((resolve, reject) => {
    request.get(characterUri, (error, response, body) => {
      if (error) {
        console.log('Error: ', error);
        reject(error);
      } else {
        const character = JSON.parse(body);
        resolve(character.name);
      }
    });
  });
};

/**
 * Main function to fetch movie data and print character names
 */
const main = async () => {
  // Fetch the list of character URIs from the movie API
  const charactersUri = await new Promise((resolve, reject) => {
    request.get(filmUri, (error, response, body) => {
      if (error) {
        console.log('Error: ', error);
        reject(error);
      } else {
        resolve(JSON.parse(body).characters);
      }
    });
  });

  // Iterate over each character URI and print their name
  for (const characterUri of charactersUri) {
    const name = await printCharacterName(characterUri).catch((error) => {
      console.log(error);
    });
    console.log(name);
  }
};

// Call the main function to start fetching and printing character names
main();