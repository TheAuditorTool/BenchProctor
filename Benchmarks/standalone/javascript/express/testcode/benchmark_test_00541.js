// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00541(req, res) {
  const userInput = req.body.payload || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const fileContent = fs.readFileSync("/var/app/data/" + data, "utf8");
  res.send(fileContent);
}

module.exports = { BenchmarkTest00541 };
