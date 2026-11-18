// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function compactSchedule(req, res) {
  const footnote = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const trim = (v) => String(v).trim();
  const bulletin = trim(footnote);
  const { PrismaClient } = require("@prisma/client");
  const _prisma = (globalThis._prisma ??= new PrismaClient());
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + bulletin + "'");
  res.json({ done: true });
}

module.exports = { compactSchedule };
