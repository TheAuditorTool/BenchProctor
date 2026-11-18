// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function exportDigest(req, res) {
  const blurb = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const trim = (v) => String(v).trim();
  const handshake = trim(blurb);
  const { Sequelize } = require("sequelize");
  const _sequelize = (globalThis._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
  await _sequelize.query("SELECT * FROM users WHERE id = '" + handshake + "'");
  res.json({ done: true });
}

module.exports = { exportDigest };
