// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00324(req, res) {
  const userInput = (req && req.file && req.file.originalname) || "";
  const [data] = String(userInput).split(',');
  const fileContent = fs.readFileSync("/var/app/data/" + data, "utf8");
  res.send(fileContent);
}

module.exports = { BenchmarkTest00324 };
