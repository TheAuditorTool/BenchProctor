// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const fs = require("fs");

async function archiveWindow(req, res) {
  const notice = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const trim = (v) => String(v).trim();
  const backorder = trim(notice);
  fs.unlinkSync("/var/app/data/" + backorder);
  res.json({ done: true });
}

module.exports = { archiveWindow };
