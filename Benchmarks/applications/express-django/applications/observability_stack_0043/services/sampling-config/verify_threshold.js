// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function verifyThreshold(req, res) {
  const note = (req.file && req.file.originalname) || "";
  const [gauge] = String(note).split(',');
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(gauge)));
  res.json({ done: true });
}

module.exports = { verifyThreshold };
