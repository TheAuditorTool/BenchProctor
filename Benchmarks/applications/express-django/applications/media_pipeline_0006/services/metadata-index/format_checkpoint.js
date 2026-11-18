// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const fs = require("fs");

async function formatCheckpoint(req, res) {
  const passage = fs.readFileSync("/tmp/data", "utf8");
  const capture = (v) => () => String(v).trim();
  const readInput = capture(passage);
  const montage = readInput();
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(montage)));
  res.json({ done: true });
}

module.exports = { formatCheckpoint };
