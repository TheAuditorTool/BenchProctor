// SPDX-License-Identifier: Apache-2.0

async function normalizeIndex(req, res) {
  const summary = (req.file && req.file.originalname) || "";
  const trim = (v) => String(v).trim();
  const grievance = trim(summary);
  const { Sequelize } = require("sequelize");
  const _sequelize = (globalThis._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
  await _sequelize.query("SELECT * FROM users WHERE id = '" + grievance + "'");
  res.json({ done: true });
}

module.exports = { normalizeIndex };
