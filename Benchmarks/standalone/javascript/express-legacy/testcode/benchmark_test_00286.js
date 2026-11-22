// SPDX-License-Identifier: Apache-2.0
const crypto = require("crypto");

async function BenchmarkTest00286(req, res) {
  const userInput = req.body.field || "";
  const data = `${userInput}`;
  const digest = await crypto.subtle.digest("SHA-256", Buffer.from(String(data)));
  res.json({ fingerprint: Buffer.from(digest).toString("hex") }); return;
}

module.exports = { BenchmarkTest00286 };
