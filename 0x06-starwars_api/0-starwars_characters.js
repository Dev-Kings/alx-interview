#!/usr/bin/node

const request = require('request');

const argv = process.argv;
const urlFilm = 'https://swapi-api.hbtn.io/api/films/';
const urlMovie = `${urlFilm}${argv[2]}/`;

// Making HTTP GET request to the API endpoint for the specified movie
request(urlMovie, function (error, response, body) {
  if (error == null) {
    // Parsing the response body into a JavaScript object
    const filmData = JSON.parse(body);
    // Fetching characters appearing in selected movie and storing in characters array
    // Contains URLs to API endpoints for each character appearing in the movie. (Charater is a list of URLs)
    const characters = filmData.characters;

    if (characters && characters.length > 0) {
      const numberOfCharacters = characters.length;
      // Initiating the character request process starting from the url of the first character
      FetchCharacter(0, characters[0], characters, numberOfCharacters);
    }
  } else {
    console.log(error);
  }
});

// Function to recursively make requests for each character and print their names
function FetchCharacter (idx, url, characters, numberOfCharacters) {
  // Base case: if index reaches the limit, stop recursion
  if (idx === numberOfCharacters) {
    return;
  }
  // Making GET request to the character's API endpoint
  request(url, function (error, response, body) {
    if (!error) {
      const characterData = JSON.parse(body);
      console.log(characterData.name);
      idx++; // increment index for next char request

      // Making a recursive call to fetch the next character
      FetchCharacter(idx, characters[idx], characters, numberOfCharacters);
    } else {
      console.error('error:', error);
    }
  });
}
