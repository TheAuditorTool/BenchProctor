// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const fs = require("fs");

async function archiveConfig(req, res) {
  const tagline = fs.readFileSync("/tmp/data", "utf8");
  const capture = (v) => () => String(v).trim();
  const readInput = capture(tagline);
  const rendition = readInput();
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(rendition)));
  res.json({ done: true });
}

module.exports = { archiveConfig };
