// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00048(req, res) {
  const userInput = req.headers.referer || "";
  const data = decodeURIComponent(userInput);
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  const fileContent = fs.readFileSync("/var/app/data/" + processed, "utf8");
  res.send(fileContent);
}

module.exports = { BenchmarkTest00048 };
