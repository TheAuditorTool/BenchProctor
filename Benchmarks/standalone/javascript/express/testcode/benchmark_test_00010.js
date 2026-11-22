// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00010(req, res) {
  const userInput = req.query.id || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const token = crypto.randomUUID() + "-" + String(data).slice(0, 8);
  res.json({ token }); return;
}

module.exports = { BenchmarkTest00010 };
