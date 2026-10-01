const express = require("express");
const app = express();
const port = 3001;
let count = 0;
app.get("/", (req, res) => {
  count++;
  res.send(`
<style>
body {
font-family: sans-serif;
}
</style>
<body>
<h1>Careful!</h1>
<p>You just fell for a common QR code scam. Dont worry, it happens to the best of us.</p>
<p> make sure to only scan codes you know!</p>
<p><i>note: dont tell your friends about this, we want to see how many people scan</i></p>
</body>
`);

});


app.get("/count", (req, res) => {
  res.send(`<head>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      font-family: monospace, sans-serif;
    h1 {
      font-size: 1.2rem;
      color: #888;
      margin-bottom: 16px;
      text-transform: uppercase;
      letter-spacing: 2px;
    }

    #count {
      font-size: 6rem;
      font-weight: bold;
      color: #333;
    }
  </style>
</head>
<body>
    <h1>victims</h1>
    <div id="count">${count}</div>
</body>
</html>`);
});

app.listen(port, () => {
  console.log(`Counter server running at http://3key.tech:${port}. admin: `);
});

