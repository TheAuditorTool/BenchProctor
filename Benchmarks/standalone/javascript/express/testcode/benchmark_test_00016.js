// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const crypto = require("crypto");

async function BenchmarkTest00016(req, res) {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const token = crypto.randomBytes(16).toString("hex");
  res.json({ token, label: String(userInput) });
}

module.exports = { BenchmarkTest00016 };
