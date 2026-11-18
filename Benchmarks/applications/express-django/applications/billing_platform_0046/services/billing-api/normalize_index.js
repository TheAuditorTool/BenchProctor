// SPDX-License-Identifier: Apache-2.0
const { db, escapeHtml } = require("./shared");

async function normalizeIndex(req, res) {
  const remark = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  function normalize(value) { return String(value).normalize("NFC"); }
  const remittance = normalize(remark);
  res.send(escapeHtml(remittance));
}

module.exports = { normalizeIndex };
