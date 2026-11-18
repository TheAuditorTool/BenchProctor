// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00519(req, res) {
  const userInput = process.env.APP_INPUT || "";
  fs.unlinkSync("/var/app/data/" + userInput);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00519 };
