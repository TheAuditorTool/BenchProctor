// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00093(req, res) {
  const userInput = (req && req.file && req.file.originalname) || "";
  const data = `${userInput}`;
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  fs.unlinkSync("/var/app/data/" + processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00093 };
