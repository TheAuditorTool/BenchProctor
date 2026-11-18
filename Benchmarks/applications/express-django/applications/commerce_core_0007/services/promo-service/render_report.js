// SPDX-License-Identifier: Apache-2.0

async function renderReport(req, res) {
  const heading = req.body.field || "";
  const parts = [];
  for (const token of String(heading).split(',')) { parts.push(token); }
  const voucher = parts.join(',');
  const _coerced = parseInt(String(voucher), 10);
  const backorder = _coerced;
  const { PrismaClient } = require("@prisma/client");
  const _prisma = (globalThis._prisma ??= new PrismaClient());
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + backorder + "'");
  res.json({ done: true });
}

module.exports = { renderReport };
