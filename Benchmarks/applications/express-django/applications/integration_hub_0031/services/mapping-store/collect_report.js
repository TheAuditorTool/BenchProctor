// SPDX-License-Identifier: Apache-2.0

async function collectReport(req, res) {
  const snippet = req.body.field || "";
  const parts = [];
  for (const token of String(snippet).split(',')) { parts.push(token); }
  const handshake = parts.join(',');
  const _coerced = parseInt(String(handshake), 10);
  const paragraph = _coerced;
  const { Sequelize } = require("sequelize");
  const _sequelize = (globalThis._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
  await _sequelize.query("SELECT * FROM users WHERE id = '" + paragraph + "'");
  res.json({ done: true });
}

module.exports = { collectReport };
