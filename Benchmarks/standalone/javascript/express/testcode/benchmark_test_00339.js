// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00339(req, res) {
  const userInput = req.params.id || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const token = crypto.randomBytes(16).toString("hex");
  res.json({ token, label: String(data) });
}

module.exports = { BenchmarkTest00339 };
