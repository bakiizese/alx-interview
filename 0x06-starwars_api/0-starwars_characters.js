#!/usr/bin/node

const request = require('request');
const args = process.argv.slice(2);

const movieId = args[0];
const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

const getMovieDetails = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Failed to load page, status code: ${response.statusCode}`));
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
};

const getCharacterName = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Failed to load page, status code: ${response.statusCode}`));
      } else {
        const character = JSON.parse(body);
        resolve(character.name);
      }
    });
  });
};

const displayCharacterNames = async () => {
  try {
    const movieDetails = await getMovieDetails(filmUrl);
    const characterPromises = movieDetails.characters.map((url) => getCharacterName(url));
    const characterNames = await Promise.all(characterPromises);

    characterNames.forEach((name) => {
      console.log(name);
    });
  } catch (error) {
    console.error('Error:', error.message);
  }
};
displayCharacterNames();
