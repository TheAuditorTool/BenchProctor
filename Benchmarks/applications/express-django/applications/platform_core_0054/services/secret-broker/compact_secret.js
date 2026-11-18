// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function compactSecret(req, res) {
  const snippet = (req.file && req.file.originalname) || "";
  const [persona] = String(snippet).split(',');
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(persona)));
  res.json({ done: true });
}

module.exports = { compactSecret };
