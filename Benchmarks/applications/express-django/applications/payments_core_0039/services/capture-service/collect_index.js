// SPDX-License-Identifier: Apache-2.0

async function collectIndex(req, res) {
  const { createClient } = require("redis");
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const memo = (await _cache.get("user_data")) || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(memo);
  const ledger = readInput();
  const { PrismaClient } = require("@prisma/client");
  const _prisma = (globalThis._prisma ??= new PrismaClient());
  await _prisma.$executeRawUnsafe("UPDATE users SET locked = 0 WHERE name = $1", ledger);
  res.json({ done: true });
}

module.exports = { collectIndex };
