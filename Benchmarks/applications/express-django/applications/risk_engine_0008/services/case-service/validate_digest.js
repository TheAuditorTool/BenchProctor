// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const fs = require("fs");

async function validateDigest(req, res) {
  const synopsis = fs.readFileSync("/tmp/data", "utf8");
  const capture = (v) => () => String(v).trim();
  const readInput = capture(synopsis);
  const verdict = readInput();
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(verdict)));
  res.json({ done: true });
}

module.exports = { validateDigest };
