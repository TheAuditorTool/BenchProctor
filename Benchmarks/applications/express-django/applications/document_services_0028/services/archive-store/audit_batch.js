// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function auditBatch(req, res) {
  const note = (req.file && req.file.originalname) || "";
  const [addendum] = String(note).split(',');
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(addendum)));
  res.json({ done: true });
}

module.exports = { auditBatch };
