// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00354(req, res) {
  const userInput = req.headers.host || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  fs.writeFileSync("/var/uploads/" + data, "data");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00354 };
