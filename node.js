import express from 'express';
import fs from 'fs';
import ollama from 'ollama';

async function generateText() {
    //const response = await ollama.generate({
    //    model: 'llama3', // Specify the model you want to use
    //    prompt: 'hi', // Your prompt
    //});
    console.log("Hello World!");
    //console.log(response.text); // Print the generated text
}

generateText();
//const app = express();
//app.get('/', (request, response) => {
//    fs.readFile('index.html', 'utf8', (err, html) => {
//
//        if (err) {
//            response.status(500).send('sorry, out of order');
//        }
//
//        response.send(html);
//    })
//});
//
//app.listen(process.env.PORT || 5000, () => console.log('listening on port 5000'));
