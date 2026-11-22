// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00210(req, res) {
  const userInput = req.headers.authorization || "";
  const data = userInput != null ? userInput : '';
  const fileContent = fs.readFileSync("/var/app/data/" + data, "utf8");
  res.send(fileContent);
}

module.exports = { BenchmarkTest00210 };
