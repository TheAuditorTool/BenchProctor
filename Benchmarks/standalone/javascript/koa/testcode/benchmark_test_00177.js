// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00177 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const [data] = String(userInput).split(',');
  const { PrismaClient } = require("@prisma/client");
  const _prisma = new PrismaClient();
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + data + "'");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00177 };
