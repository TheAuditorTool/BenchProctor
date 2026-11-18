// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00408(req, res) {
  const userInput = req.query.id || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(data)));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00408 };
