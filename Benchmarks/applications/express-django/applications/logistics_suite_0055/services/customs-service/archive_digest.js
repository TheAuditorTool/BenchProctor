// SPDX-License-Identifier: Apache-2.0
const { db, escapeHtml } = require("./shared");

async function archiveDigest(req, res) {
  const heading = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  function normalize(value) { return String(value).normalize("NFC"); }
  const consignment = normalize(heading);
  res.send(escapeHtml(consignment));
}

module.exports = { archiveDigest };
