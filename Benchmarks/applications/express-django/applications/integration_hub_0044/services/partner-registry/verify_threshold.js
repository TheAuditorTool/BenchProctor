// SPDX-License-Identifier: Apache-2.0

async function verifyThreshold(req, res) {
  const { createClient } = require("redis");
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const blurb = (await _cache.get("user_data")) || "";
  const tokens = String(blurb).split(',').filter((t) => t.length > 0);
  const handshake = tokens.join(' ');
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(handshake)) { res.status(400).json({error:"invalid"}); return; }
  const citation = handshake;
  const { Sequelize } = require("sequelize");
  const _sequelize = (globalThis._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
  await _sequelize.query("SELECT * FROM users WHERE id = '" + citation + "'");
  res.json({ done: true });
}

module.exports = { verifyThreshold };
