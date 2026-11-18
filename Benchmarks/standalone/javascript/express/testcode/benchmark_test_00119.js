// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00119(req, res) {
  const userInput = req.headers.authorization || "";
  const data = userInput != null ? userInput : '';
  crypto.createHash("sha256").update(data).digest("hex");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00119 };
