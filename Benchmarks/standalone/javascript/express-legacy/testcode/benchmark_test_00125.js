// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function BenchmarkTest00125(req, res) {
  const userInput = fs.readFileSync("/tmp/data", "utf8");
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  const { PrismaClient } = require("@prisma/client");
  const _prisma = new PrismaClient();
  await _prisma.$executeRawUnsafe("UPDATE users SET locked = 0 WHERE name = '" + data + "'");
  res.json({ done: true });
}

module.exports = { BenchmarkTest00125 };
