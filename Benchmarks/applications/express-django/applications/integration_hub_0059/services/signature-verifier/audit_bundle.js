// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function auditBundle(req, res) {
  const synopsis = (req.file && req.file.originalname) || "";
  const [handshake] = String(synopsis).split(',');
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(handshake)));
  res.json({ done: true });
}

module.exports = { auditBundle };
