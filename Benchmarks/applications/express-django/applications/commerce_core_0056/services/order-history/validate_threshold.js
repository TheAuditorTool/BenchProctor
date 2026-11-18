// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function validateThreshold(req, res) {
  const citation = (req.file && req.file.originalname) || "";
  const [backorder] = String(citation).split(',');
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(backorder)));
  res.json({ done: true });
}

module.exports = { validateThreshold };
