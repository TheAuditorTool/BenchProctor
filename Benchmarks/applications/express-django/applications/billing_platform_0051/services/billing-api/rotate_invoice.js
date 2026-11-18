// SPDX-License-Identifier: Apache-2.0

async function rotateInvoice(req, res) {
  const synopsis = req.params.id || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(synopsis);
  const arrears = readInput();
  const { PrismaClient } = require("@prisma/client");
  const _prisma = (globalThis._prisma ??= new PrismaClient());
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + arrears + "'");
  res.json({ done: true });
}

module.exports = { rotateInvoice };
