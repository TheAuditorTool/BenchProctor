// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const fs = require("fs");

async function summarizeThreshold(req, res) {
  const snippet = fs.readFileSync("/tmp/data", "utf8");
  const capture = (v) => () => String(v).trim();
  const readInput = capture(snippet);
  const handshake = readInput();
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(handshake)));
  res.json({ done: true });
}

module.exports = { summarizeThreshold };
