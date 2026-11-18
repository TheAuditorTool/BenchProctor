// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function buildSummary(req, res) {
  const synopsis = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const trim = (v) => String(v).trim();
  const verdict = trim(synopsis);
  const { Sequelize } = require("sequelize");
  const _sequelize = (globalThis._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
  await _sequelize.query("SELECT * FROM users WHERE id = '" + verdict + "'");
  res.json({ done: true });
}

module.exports = { buildSummary };
