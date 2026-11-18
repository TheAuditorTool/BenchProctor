// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function reconcileRecord(req, res) {
  const subject = (req.file && req.file.originalname) || "";
  const [grievance] = String(subject).split(',');
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(grievance)));
  res.json({ done: true });
}

module.exports = { reconcileRecord };
