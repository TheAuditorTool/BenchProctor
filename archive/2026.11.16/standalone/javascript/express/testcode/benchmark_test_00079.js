// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00079(req, res) {
  const userInput = (req.file && req.file.originalname) || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^[a-zA-Z0-9 _.#~\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  fs.writeFileSync("/var/uploads/" + processed, "data");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00079 };
