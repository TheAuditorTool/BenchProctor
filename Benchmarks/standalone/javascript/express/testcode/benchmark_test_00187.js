// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00187(req, res) {
  const userInput = req.body?.multipart_field || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  fs.unlinkSync("/var/app/data/" + data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00187 };
