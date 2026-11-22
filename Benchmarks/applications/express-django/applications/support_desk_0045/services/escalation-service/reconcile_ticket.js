// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function reconcileTicket(req, res) {
  const remark = req.body?.payload || "";
  const tokens = String(remark).split(',').filter((t) => t.length > 0);
  const inquiry = tokens.join(' ');
  const { escapeIdentifier } = require("pg");
  await db.query("SELECT * FROM users ORDER BY " + escapeIdentifier(String(inquiry)));
  res.json({ done: true });
}

module.exports = { reconcileTicket };
