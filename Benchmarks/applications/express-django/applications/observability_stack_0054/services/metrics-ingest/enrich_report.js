// SPDX-License-Identifier: Apache-2.0

async function enrichReport(req, res) {
  const excerpt = req.headers["user-agent"] || "";
  const cohort = excerpt != null ? excerpt : '';
  const knex = require("knex");
  const _knex = (globalThis._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.raw("SELECT * FROM users WHERE id = '" + cohort + "'");
  res.json({ done: true });
}

module.exports = { enrichReport };
