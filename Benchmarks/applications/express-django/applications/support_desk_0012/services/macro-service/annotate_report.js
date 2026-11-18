// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function annotateReport(req, res) {
  const summary = (req.file && req.file.originalname) || "";
  const [grievance] = String(summary).split(',');
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(grievance)));
  res.json({ done: true });
}

module.exports = { annotateReport };
