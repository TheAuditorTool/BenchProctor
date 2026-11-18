// SPDX-License-Identifier: Apache-2.0
const { db, escapeHtml } = require("./shared");

async function auditSummary(req, res) {
  const footnote = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  function normalize(value) { return String(value).normalize("NFC"); }
  const bulletin = normalize(footnote);
  res.send(escapeHtml(bulletin));
}

module.exports = { auditSummary };
