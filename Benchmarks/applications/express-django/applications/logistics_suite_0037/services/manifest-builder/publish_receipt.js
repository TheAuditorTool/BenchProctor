// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function publishReceipt(req, res) {
  const footnote = (req.file && req.file.originalname) || "";
  const [consignment] = String(footnote).split(',');
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(consignment)));
  res.json({ done: true });
}

module.exports = { publishReceipt };
