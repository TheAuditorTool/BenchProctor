// SPDX-License-Identifier: Apache-2.0

async function formatBundle(req, res) {
  const citation = req.params.id || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(citation);
  const backorder = readInput();
  const { PrismaClient } = require("@prisma/client");
  const _prisma = (globalThis._prisma ??= new PrismaClient());
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + backorder + "'");
  res.json({ done: true });
}

module.exports = { formatBundle };
