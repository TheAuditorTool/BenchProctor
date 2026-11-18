// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const fs = require("fs");

async function auditSchedule(req, res) {
  const preface = fs.readFileSync("/tmp/data", "utf8");
  const capture = (v) => () => String(v).trim();
  const readInput = capture(preface);
  const bulletin = readInput();
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(bulletin)));
  res.json({ done: true });
}

module.exports = { auditSchedule };
