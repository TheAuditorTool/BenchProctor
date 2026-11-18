// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00466(req, res) {
  const userInput = req.body || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  crypto.createHash("sha256").update(data).digest("hex");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00466 };
