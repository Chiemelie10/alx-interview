#!/usr/bin/node
/**
 * Prints all characters of a Star Wars movie
 * The first positional argument passed is the Movie ID
 * Display one character name per line in the same order
 * as'characters' list in the /films/ endpoint.
 */

const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;
request(url, async function (error, response, body) {
  if (error) {
    return console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character in characters) {
      const res = await new Promise((resolve, reject) => {
        request(characters[character], (err, res, html) => {
          if (err) {
            reject(err);
          } else {
            resolve(JSON.parse(html).name);
          }
        });
      });
      console.log(res);
    }
  }
});
