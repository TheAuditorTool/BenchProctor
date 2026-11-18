// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function normalizeSnapshot(req, res) {
  const headline = (req.file && req.file.originalname) || "";
  const [disbursement] = String(headline).split(',');
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(disbursement)));
  res.json({ done: true });
}

module.exports = { normalizeSnapshot };
