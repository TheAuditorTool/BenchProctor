// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function pruneReport(req, res) {
  const remark = req.body?.payload || "";
  const tokens = String(remark).split(',').filter((t) => t.length > 0);
  const note = tokens.join(' ');
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(note)));
  res.json({ done: true });
}

module.exports = { pruneReport };
