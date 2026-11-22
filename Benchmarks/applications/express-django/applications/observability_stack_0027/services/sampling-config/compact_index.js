// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function compactIndex(req, res) {
  const remark = req.body.payload || "";
  const tokens = String(remark).split(',').filter((t) => t.length > 0);
  const gauge = tokens.join(' ');
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(gauge)));
  res.json({ done: true });
}

module.exports = { compactIndex };
