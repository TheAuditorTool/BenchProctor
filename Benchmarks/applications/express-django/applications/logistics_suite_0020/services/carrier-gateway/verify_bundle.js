// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function verifyBundle(req, res) {
  const transcript = req.body?.payload || "";
  const tokens = String(transcript).split(',').filter((t) => t.length > 0);
  const consignment = tokens.join(' ');
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(consignment)));
  res.json({ done: true });
}

module.exports = { verifyBundle };
