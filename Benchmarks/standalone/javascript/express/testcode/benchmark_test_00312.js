// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00312(req, res) {
  const userInput = req.body.payload || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  const fileContent = fs.readFileSync("/var/app/data/" + data, "utf8");
  res.send(fileContent);
}

module.exports = { BenchmarkTest00312 };
