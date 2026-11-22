// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00187(req, res) {
  const userInput = req.params.id || "";
  const data = `${userInput}`;
  fs.unlinkSync("/var/app/data/" + data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00187 };
