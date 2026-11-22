// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function annotateSnapshot(req, res) {
  const memo = req.body.payload || "";
  const tokens = String(memo).split(',').filter((t) => t.length > 0);
  const backorder = tokens.join(' ');
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(backorder)));
  res.json({ done: true });
}

module.exports = { annotateSnapshot };
