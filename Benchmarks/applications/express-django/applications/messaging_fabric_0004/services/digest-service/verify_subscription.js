// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function verifySubscription(req, res) {
  const paragraph = (req.file && req.file.originalname) || "";
  const [bulletin] = String(paragraph).split(',');
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(bulletin)));
  res.json({ done: true });
}

module.exports = { verifySubscription };
