// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00065(req, res) {
  const userInput = req.body || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const fileContent = fs.readFileSync("/var/app/data/" + data, "utf8");
  res.send(fileContent);
}

module.exports = { BenchmarkTest00065 };
