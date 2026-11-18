// SPDX-License-Identifier: Apache-2.0

async function publishDigest(req, res) {
  const citation = req.body.field || "";
  const parts = [];
  for (const token of String(citation).split(',')) { parts.push(token); }
  const backorder = parts.join(',');
  const _coerced = parseInt(String(backorder), 10);
  const restock = _coerced;
  const { PrismaClient } = require("@prisma/client");
  const _prisma = (globalThis._prisma ??= new PrismaClient());
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + restock + "'");
  res.json({ done: true });
}

module.exports = { publishDigest };
