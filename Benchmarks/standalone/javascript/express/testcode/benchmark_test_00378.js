// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00378(req, res) {
  const userInput = req.body.payload || "";
  const _raw = userInput;
  const data = (_raw && _raw.length > 0) ? _raw : 'default';
  const token = crypto.randomBytes(16).toString("hex");
  res.json({ token, label: String(data) });
}

module.exports = { BenchmarkTest00378 };
