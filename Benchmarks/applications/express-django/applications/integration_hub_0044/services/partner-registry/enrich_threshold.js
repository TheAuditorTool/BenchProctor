// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function enrichThreshold(req, res) {
  const blurb = (req.file && req.file.originalname) || "";
  const [handshake] = String(blurb).split(',');
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(handshake)));
  res.json({ done: true });
}

module.exports = { enrichThreshold };
