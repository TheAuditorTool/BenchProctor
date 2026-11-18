// SPDX-License-Identifier: Apache-2.0
const { db, escapeHtml } = require("./shared");

async function compactReceipt(req, res) {
  const synopsis = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  function normalize(value) { return String(value).normalize("NFC"); }
  const arrears = normalize(synopsis);
  res.send(escapeHtml(arrears));
}

module.exports = { compactReceipt };
