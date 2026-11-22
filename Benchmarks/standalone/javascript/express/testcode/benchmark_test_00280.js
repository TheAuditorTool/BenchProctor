// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00280(req, res) {
  const userInput = req.headers.authorization || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  const fileContent = fs.readFileSync("/var/app/data/" + data, "utf8");
  res.send(fileContent);
}

module.exports = { BenchmarkTest00280 };
