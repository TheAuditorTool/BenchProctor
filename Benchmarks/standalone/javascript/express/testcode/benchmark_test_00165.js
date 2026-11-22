// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00165(req, res) {
  const userInput = req.headers["user-agent"] || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const digest = await crypto.subtle.digest("SHA-256", Buffer.from(String(data)));
  res.json({ fingerprint: Buffer.from(digest).toString("hex") }); return;
}

module.exports = { BenchmarkTest00165 };
