// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00253(req, res) {
  const userInput = req.body || "";
  const data = String(userInput).slice(0, 200);
  fs.unlinkSync("/var/app/data/" + data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00253 };
