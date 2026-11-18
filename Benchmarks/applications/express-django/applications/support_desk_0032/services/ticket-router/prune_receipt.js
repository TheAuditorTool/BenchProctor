// SPDX-License-Identifier: Apache-2.0
const { db, escapeHtml } = require("./shared");

async function pruneReceipt(req, res) {
  const note = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  function normalize(value) { return String(value).normalize("NFC"); }
  const inquiry = normalize(note);
  res.send(escapeHtml(inquiry));
}

module.exports = { pruneReceipt };
