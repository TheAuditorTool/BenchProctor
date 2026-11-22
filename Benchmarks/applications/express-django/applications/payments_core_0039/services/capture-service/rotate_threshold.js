// SPDX-License-Identifier: Apache-2.0

async function rotateThreshold(req, res) {
  const memo = req.cookies.session_token || "";
  const ledger = Buffer.from(memo, "base64").toString();
  const { PrismaClient } = require("@prisma/client");
  const _prisma = (globalThis._prisma ??= new PrismaClient());
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + ledger + "'");
  res.json({ done: true });
}

module.exports = { rotateThreshold };
