// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");
const path = require("path");

async function BenchmarkTest00051(req, res) {
  const userInput = req.headers.referer || "";
  const data = `${userInput}`;
  const checkedPath = "/var/app/data/" + path.basename(data);
  const fileContent = fs.readFileSync(checkedPath, "utf8");
  res.send(fileContent);
}

module.exports = { BenchmarkTest00051 };
