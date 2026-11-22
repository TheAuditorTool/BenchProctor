// SPDX-License-Identifier: Apache-2.0

async function auditStock(req, res) {
  const memo = req.cookies.session_token || "";
  const backorder = Buffer.from(memo, "base64").toString();
  const knex = require("knex");
  const _knex = (globalThis._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.raw("SELECT * FROM users WHERE id = '" + backorder + "'");
  res.json({ done: true });
}

module.exports = { auditStock };
