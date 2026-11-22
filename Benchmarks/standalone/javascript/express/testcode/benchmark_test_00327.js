// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00327(req, res) {
  const userInput = req.body?.field || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const fileContent = fs.readFileSync("/var/app/data/" + data, "utf8");
  res.send(fileContent);
}

module.exports = { BenchmarkTest00327 };
