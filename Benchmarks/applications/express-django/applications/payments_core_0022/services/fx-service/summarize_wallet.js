// SPDX-License-Identifier: Apache-2.0
const { db, escapeHtml } = require("./shared");

async function summarizeWallet(req, res) {
  const subject = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  function normalize(value) { return String(value).normalize("NFC"); }
  const ledger = normalize(subject);
  res.send(escapeHtml(ledger));
}

module.exports = { summarizeWallet };
