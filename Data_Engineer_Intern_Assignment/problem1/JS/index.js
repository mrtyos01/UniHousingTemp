/*
@author: MortezaYosefy

To work with a file system, you need to install file system package first.

Install file system with the following command:

    npm install

If you dont have node run time in your device, please install it first from the link below: 
     :https://nodejs.org/en/
*/

const json = require("./problem1.json");
const fs = require("fs");

function objectFrom() {
  let ujson = json.map((item) => {
    const rno = {}; //return new object
    Object.keys(item).forEach((key) => {
      if (!item[key]) rno[key] = null;
      else rno[key] = item[key];
    });
    return rno;
  });
  return ujson;
}


const njson = JSON.stringify(objectFrom());

// Here we write the json file with null at the same directory
fs.writeFile("./newfile.json", njson, (er) => {
  console.log(er);
});


/*
Open a terminal where your working directory is and run the following commad:

     node index.js

Now you can check file.json file and all of empty string are replaced with null.
*/
