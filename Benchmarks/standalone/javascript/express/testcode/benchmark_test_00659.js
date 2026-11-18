// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00659(req, res) {
  const userInput = req.body.payload || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(data)));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00659 };
