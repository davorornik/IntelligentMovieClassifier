import {handler} from './build/handler.js';
import express from 'express';

const app = express();

app.use(express.json());

app.post('/evaluate', (req, res) => {

    //  note import tensorflow
    res.json(req.body);
});

// let SvelteKit handle everything else, including serving prerendered pages and static assets
app.use(handler);

app.listen(3000);