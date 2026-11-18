// SPDX-License-Identifier: Apache-2.0
const { db, escapeHtml } = require("./shared");

async function summarizeSchedule(req, res) {
  const summary = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  function normalize(value) { return String(value).normalize("NFC"); }
  const restock = normalize(summary);
  res.send(escapeHtml(restock));
}

module.exports = { summarizeSchedule };
