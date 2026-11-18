// SPDX-License-Identifier: Apache-2.0
const { db, escapeHtml } = require("./shared");

async function reconcileConfig(req, res) {
  const passage = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  function normalize(value) { return String(value).normalize("NFC"); }
  const persona = normalize(passage);
  res.send(escapeHtml(persona));
}

module.exports = { reconcileConfig };
