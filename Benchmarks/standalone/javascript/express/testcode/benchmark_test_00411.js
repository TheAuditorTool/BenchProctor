// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00411(req, res) {
  const userInput = req.query.id || "";
  const fileContent = fs.readFileSync("/var/app/data/" + userInput, "utf8");
  res.send(fileContent);
}

module.exports = { BenchmarkTest00411 };
