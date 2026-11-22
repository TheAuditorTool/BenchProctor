// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

const BenchmarkTest00107 = async (ctx) => {
  const userInput = fs.readFileSync("/tmp/data", "utf8");
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  const { PrismaClient } = require("@prisma/client");
  const _prisma = new PrismaClient();
  await _prisma.$executeRawUnsafe("UPDATE users SET locked = 0 WHERE name = '" + data + "'");
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00107 };
