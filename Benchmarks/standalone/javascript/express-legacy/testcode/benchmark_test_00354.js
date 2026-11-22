// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00354(req, res) {
  const userInput = req.body.payload || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  fs.unlinkSync("/var/app/data/" + data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00354 };
