// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function auditReceipt(req, res) {
  const citation = (req.file && req.file.originalname) || "";
  const [parcel] = String(citation).split(',');
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(parcel)));
  res.json({ done: true });
}

module.exports = { auditReceipt };
