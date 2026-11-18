// SPDX-License-Identifier: Apache-2.0

async function loadWindow(req, res) {
  const heading = (req.file && req.file.originalname) || "";
  const trim = (v) => String(v).trim();
  const voucher = trim(heading);
  const { PrismaClient } = require("@prisma/client");
  const _prisma = (globalThis._prisma ??= new PrismaClient());
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + voucher + "'");
  res.json({ done: true });
}

module.exports = { loadWindow };
