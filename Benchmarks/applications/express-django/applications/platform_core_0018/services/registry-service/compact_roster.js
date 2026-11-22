// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function compactRoster(req, res) {
  const subtitle = req.body?.payload || "";
  const tokens = String(subtitle).split(',').filter((t) => t.length > 0);
  const persona = tokens.join(' ');
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(persona)));
  res.json({ done: true });
}

module.exports = { compactRoster };
