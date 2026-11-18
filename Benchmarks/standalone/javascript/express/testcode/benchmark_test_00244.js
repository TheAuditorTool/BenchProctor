// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00244(req, res) {
  const userInput = req.body.payload || "";
  const token = crypto.randomBytes(16).toString("hex");
  res.json({ token, label: String(userInput) });
}

module.exports = { BenchmarkTest00244 };
