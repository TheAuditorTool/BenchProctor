// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00093(req, res) {
  const userInput = req.headers.referer || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const fileContent = fs.readFileSync("/var/app/data/" + data, "utf8");
  res.send(fileContent);
}

module.exports = { BenchmarkTest00093 };
