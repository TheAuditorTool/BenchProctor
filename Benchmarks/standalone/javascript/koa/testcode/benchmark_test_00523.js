// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00523 = async (ctx) => {
  const userInput = fs.readFileSync("/tmp/data", "utf8");
  const data = userInput != null ? userInput : '';
  const { PrismaClient } = require("@prisma/client");
  const _prisma = new PrismaClient();
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + data + "'");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00523 };
