// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function loadIndex(req, res) {
  const synopsis = (req.file && req.file.originalname) || "";
  const [verdict] = String(synopsis).split(',');
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(verdict)));
  res.json({ done: true });
}

module.exports = { loadIndex };
