// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");
const nodeUtil = require("util");

async function BenchmarkTest00143(req, res) {
  const userInput = req.body.field || "";
  const data = nodeUtil.format("%s", userInput);
  const fileContent = fs.readFileSync("/var/app/data/" + data, "utf8");
  res.send(fileContent);
}

module.exports = { BenchmarkTest00143 };
