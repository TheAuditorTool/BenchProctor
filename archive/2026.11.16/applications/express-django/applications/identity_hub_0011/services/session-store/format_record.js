// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function formatRecord(req, res) {
  const excerpt = JSON.parse(fs.readFileSync("/etc/app/config.json", "utf8")).value;
  const _raw = excerpt;
  const persona = (_raw && _raw.length > 0) ? _raw : 'default';
  const { Sequelize } = require("sequelize");
  const _sequelize = (globalThis._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
  await _sequelize.query("SELECT * FROM users WHERE id = '" + persona + "'");
  res.json({ done: true });
}

module.exports = { formatRecord };
