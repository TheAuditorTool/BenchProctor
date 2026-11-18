// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00001(req, res) {
  const userInput = req.body || "";
  const data = `${userInput}`;
  fs.unlinkSync("/var/app/data/" + data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00001 };
