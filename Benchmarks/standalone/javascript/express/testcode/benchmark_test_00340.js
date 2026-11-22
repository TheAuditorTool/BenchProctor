// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00340(req, res) {
  const userInput = req.query.id || "";
  const data = String(userInput).replace(/\u0000/g, "");
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  const fileContent = fs.readFileSync("/var/app/data/" + processed, "utf8");
  res.send(fileContent);
}

module.exports = { BenchmarkTest00340 };
