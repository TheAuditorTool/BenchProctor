// SPDX-License-Identifier: Apache-2.0
const { db, escapeHtml } = require("./shared");

async function summarizeProfile(req, res) {
  const caption = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  function normalize(value) { return String(value).normalize("NFC"); }
  const ledger = normalize(caption);
  res.send(escapeHtml(ledger));
}

module.exports = { summarizeProfile };
