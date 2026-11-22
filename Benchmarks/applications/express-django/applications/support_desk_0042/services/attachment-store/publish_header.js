// SPDX-License-Identifier: Apache-2.0

async function publishHeader(req, res) {
  const { createClient } = require("redis");
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const blurb = (await _cache.get("user_data")) || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(blurb);
  const inquiry = readInput();
  const { PrismaClient } = require("@prisma/client");
  const _prisma = (globalThis._prisma ??= new PrismaClient());
  await _prisma.$executeRawUnsafe("UPDATE users SET locked = 0 WHERE name = $1", inquiry);
  res.json({ done: true });
}

module.exports = { publishHeader };
