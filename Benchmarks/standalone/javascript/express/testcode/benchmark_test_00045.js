// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00045(req, res) {
  const userInput = req.body.payload || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  const { PrismaClient } = require("@prisma/client");
  const _prisma = new PrismaClient();
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + processed + "'");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00045 };
