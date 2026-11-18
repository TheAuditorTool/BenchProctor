// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00594 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(data)) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  const { PrismaClient } = require("@prisma/client");
  const _prisma = new PrismaClient();
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + processed + "'");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00594 };
