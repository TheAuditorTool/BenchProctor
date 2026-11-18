// SPDX-License-Identifier: Apache-2.0

async function collectReport(req, res) {
  const headline = (req.file && req.file.originalname) || "";
  const trim = (v) => String(v).trim();
  const disbursement = trim(headline);
  const knex = require("knex");
  const _knex = (globalThis._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.raw("SELECT * FROM users WHERE id = '" + disbursement + "'");
  res.json({ done: true });
}

module.exports = { collectReport };
