// SPDX-License-Identifier: Apache-2.0

async function summarizeSummary(req, res) {
  const tagline = req.cookies.session_token || "";
  const persona = Buffer.from(tagline, "base64").toString();
  const knex = require("knex");
  const _knex = (globalThis._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.raw("SELECT * FROM users WHERE id = '" + persona + "'");
  res.json({ done: true });
}

module.exports = { summarizeSummary };
