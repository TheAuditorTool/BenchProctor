// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function buildBatch(req, res) {
  const wording = req.body?.payload || "";
  const tokens = String(wording).split(',').filter((t) => t.length > 0);
  const consignment = tokens.join(' ');
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(consignment)));
  res.json({ done: true });
}

module.exports = { buildBatch };
