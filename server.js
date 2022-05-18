import {handler} from './build/handler.js';
import {exec} from 'child_process';
import express from 'express';

const app = express();
app.use(express.json());


const options = {
    1: 'models/decision_tree/decision_tree.py',
    2: 'models/kNeighbors/kNeighbors.py',
    3: 'models/logistic_regression/logistic_regression.py',
    4: 'models/nn/nn.py',
    5: 'models/cnn/cnn.py'
};

app.post('/evaluate', (req, res) => {
    //  note arg is not sanitized
    const arg = `"${req.body.description}"`;
    exec(`python ${options[req.body.method]} ${arg}`,
        (error, stdout) => {
            if (error) {
                console.error(`exec error: ${error}`);
                res.json("Some error, look @Console");
                return;
            }
            res.json(stdout.trim().replace(/(\r\n|\n|\r)/gm, ", "));
        });
});

// let SvelteKit handle everything else, including serving prerendered pages and static assets
app.use(handler);

app.listen(3000);