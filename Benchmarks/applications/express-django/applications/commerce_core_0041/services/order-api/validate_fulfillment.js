// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function validateFulfillment(req, res) {
  const headline = req.body.payload || "";
  const tokens = String(headline).split(',').filter((t) => t.length > 0);
  const backorder = tokens.join(' ');
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(backorder)));
  res.json({ done: true });
}

module.exports = { validateFulfillment };
