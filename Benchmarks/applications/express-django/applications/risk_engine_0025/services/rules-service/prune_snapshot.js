// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function pruneSnapshot(req, res) {
  const excerpt = req.body?.payload || "";
  const tokens = String(excerpt).split(',').filter((t) => t.length > 0);
  const verdict = tokens.join(' ');
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(verdict)));
  res.json({ done: true });
}

module.exports = { pruneSnapshot };
