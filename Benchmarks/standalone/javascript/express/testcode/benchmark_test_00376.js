// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00376(req, res) {
  const userInput = req.body || "";
  const [data] = String(userInput).split(',');
  const { PrismaClient } = require("@prisma/client");
  const _prisma = new PrismaClient();
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + data + "'");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00376 };
