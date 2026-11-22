// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00332(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const digest = await crypto.subtle.digest("SHA-1", Buffer.from(String(data)));
  res.json({ fingerprint: Buffer.from(digest).toString("hex") }); return;
}

module.exports = { BenchmarkTest00332 };
