// SPDX-License-Identifier: Apache-2.0

async function annotateSchedule(req, res) {
  const note = req.body.field || "";
  const parts = [];
  for (const token of String(note).split(',')) { parts.push(token); }
  const handshake = parts.join(',');
  const _coerced = parseInt(String(handshake), 10);
  const persona = _coerced;
  const { Sequelize } = require("sequelize");
  const _sequelize = (globalThis._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
  await _sequelize.query("SELECT * FROM users WHERE id = '" + persona + "'");
  res.json({ done: true });
}

module.exports = { annotateSchedule };
