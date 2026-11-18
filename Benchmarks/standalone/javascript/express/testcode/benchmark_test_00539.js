// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00539(req, res) {
  const userInput = fs.readFileSync("/tmp/data", "utf8");
  const data = userInput != null ? userInput : '';
  const { PrismaClient } = require("@prisma/client");
  const _prisma = new PrismaClient();
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + data + "'");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00539 };
