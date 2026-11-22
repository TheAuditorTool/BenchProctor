// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const crypto = require("crypto");

async function BenchmarkTest00085(req, res) {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const data = String(userInput).slice(0, 200);
  const digest = await crypto.subtle.digest("SHA-256", Buffer.from(String(data)));
  res.json({ fingerprint: Buffer.from(digest).toString("hex") }); return;
}

module.exports = { BenchmarkTest00085 };
