// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");
const path = require("path");

async function BenchmarkTest00705(req, res) {
  const userInput = req.headers["x-forwarded-for"] || "";
  const [data] = String(userInput).split(',');
  const checkedPath = "/var/app/data/" + path.basename(data);
  const fileContent = fs.readFileSync(checkedPath, "utf8");
  res.send(fileContent);
}

module.exports = { BenchmarkTest00705 };
