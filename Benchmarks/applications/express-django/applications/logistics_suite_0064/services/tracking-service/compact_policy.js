// SPDX-License-Identifier: Apache-2.0
const { db, escapeHtml } = require("./shared");

async function compactPolicy(req, res) {
  const transcript = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  function normalize(value) { return String(value).normalize("NFC"); }
  const parcel = normalize(transcript);
  res.send(escapeHtml(parcel));
}

module.exports = { compactPolicy };
