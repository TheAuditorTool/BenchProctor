// SPDX-License-Identifier: Apache-2.0
const fs = require("fs");

async function collectSnapshot(req, res) {
  const preface = JSON.parse(fs.readFileSync("/etc/app/config.json", "utf8")).value;
  const _raw = preface;
  const cohort = (_raw && _raw.length > 0) ? _raw : 'default';
  const { PrismaClient } = require("@prisma/client");
  const _prisma = (globalThis._prisma ??= new PrismaClient());
  await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + cohort + "'");
  res.json({ done: true });
}

module.exports = { collectSnapshot };
