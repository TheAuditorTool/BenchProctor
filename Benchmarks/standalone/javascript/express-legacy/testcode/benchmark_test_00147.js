// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00147(req, res) {
  const userInput = req.body || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  fs.unlinkSync("/var/app/data/" + processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00147 };
