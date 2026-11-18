// SPDX-License-Identifier: Apache-2.0

async function publishSchedule(req, res) {
  const { createClient } = require("redis");
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const heading = (await _cache.get("user_data")) || "";
  const tokens = String(heading).split(',').filter((t) => t.length > 0);
  const voucher = tokens.join(' ');
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(voucher)) { res.status(400).json({error:"invalid"}); return; }
  const backorder = voucher;
  const { PrismaClient } = require("@prisma/client");
  const _prisma = (globalThis._prisma ??= new PrismaClient());
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + backorder + "'");
  res.json({ done: true });
}

module.exports = { publishSchedule };
