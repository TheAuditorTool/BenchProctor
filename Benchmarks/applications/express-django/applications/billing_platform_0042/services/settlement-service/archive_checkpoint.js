// SPDX-License-Identifier: Apache-2.0

async function archiveCheckpoint(req, res) {
  const remark = req.params.id || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(remark);
  const remittance = readInput();
  const knex = require("knex");
  const _knex = (globalThis._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.raw("SELECT * FROM users WHERE id = '" + remittance + "'");
  res.json({ done: true });
}

module.exports = { archiveCheckpoint };
