// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00114 = async (ctx) => {
  const userInput = fs.readFileSync("/tmp/data", "utf8");
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  const { PrismaClient } = require("@prisma/client");
  const { PrismaPg } = require("@prisma/adapter-pg");
  const _prisma = new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL }) });
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + data + "'");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00114 };
