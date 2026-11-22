// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00248(req, res) {
  const userInput = (req.body.variables && req.body.variables.input) || "";
  const data = `${userInput}`;
  const digest = await crypto.subtle.digest("SHA-1", Buffer.from(String(data)));
  res.json({ fingerprint: Buffer.from(digest).toString("hex") }); return;
}

module.exports = { BenchmarkTest00248 };
