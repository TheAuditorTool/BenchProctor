// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00228(req, res) {
  const userInput = req.headers.authorization || "";
  const data = `${userInput}`;
  fs.writeFileSync("/var/uploads/" + data, "data");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00228 };
