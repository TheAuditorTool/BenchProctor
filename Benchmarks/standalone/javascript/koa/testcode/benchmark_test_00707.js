// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00707 = async (ctx) => {
  const userInput = ctx.request.headers["user-agent"] || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  const { PrismaClient } = require("@prisma/client");
  const _prisma = new PrismaClient();
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + data + "'");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00707 };
