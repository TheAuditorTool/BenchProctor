// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00340(req, res) {
  const userInput = (req && req.file && req.file.originalname) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  const fileContent = fs.readFileSync("/var/app/data/" + processed, "utf8");
  res.send(fileContent);
}

module.exports = { BenchmarkTest00340 };
