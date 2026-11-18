// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function BenchmarkTest00391(req, res) {
  const userInput = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(userInput)));
  res.json({ done: true });
}

module.exports = { BenchmarkTest00391 };
