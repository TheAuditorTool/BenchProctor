// SPDX-License-Identifier: Apache-2.0

async function summarizeReport(req, res) {
  const remark = req.body.field || "";
  const parts = [];
  for (const token of String(remark).split(',')) { parts.push(token); }
  const remittance = parts.join(',');
  const _coerced = parseInt(String(remittance), 10);
  const dunning = _coerced;
  const knex = require("knex");
  const _knex = (globalThis._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.raw("SELECT * FROM users WHERE id = '" + dunning + "'");
  res.json({ done: true });
}

module.exports = { summarizeReport };
