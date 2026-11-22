// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const fs = require("fs");

async function compactSummary(req, res) {
  const subject = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const trim = (v) => String(v).trim();
  const voucher = trim(subject);
  fs.unlinkSync("/var/app/data/" + voucher);
  res.json({ done: true });
}

module.exports = { compactSummary };
