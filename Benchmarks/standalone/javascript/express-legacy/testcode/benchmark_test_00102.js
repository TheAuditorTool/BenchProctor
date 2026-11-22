// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00102(req, res) {
  const userInput = req.headers.origin || "";
  crypto.createHash("sha256").update(userInput).digest("hex");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00102 };
