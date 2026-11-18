// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00048(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const [data] = String(userInput).split(',');
  const fileContent = fs.readFileSync("/var/app/data/" + data, "utf8");
  res.send(fileContent);
}

module.exports = { BenchmarkTest00048 };
