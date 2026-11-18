// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function archiveRoster(req, res) {
  const excerpt = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const trim = (v) => String(v).trim();
  const handshake = trim(excerpt);
  const knex = require("knex");
  const _knex = (globalThis._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.raw("SELECT * FROM users WHERE id = '" + handshake + "'");
  res.json({ done: true });
}

module.exports = { archiveRoster };
