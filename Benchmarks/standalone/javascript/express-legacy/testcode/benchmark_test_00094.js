// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00094(req, res) {
  const userInput = process.env.APP_INPUT || "";
  const data = String(userInput).replace(/\u0000/g, "");
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(data)) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  const { PrismaClient } = require("@prisma/client");
  const _prisma = new PrismaClient();
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + processed + "'");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00094 };
