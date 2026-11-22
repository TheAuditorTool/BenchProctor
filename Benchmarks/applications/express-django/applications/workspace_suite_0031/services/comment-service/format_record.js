// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function formatRecord(req, res) {
  const caption = req.body?.payload || "";
  const tokens = String(caption).split(',').filter((t) => t.length > 0);
  const synopsis = tokens.join(' ');
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(synopsis)));
  res.json({ done: true });
}

module.exports = { formatRecord };
