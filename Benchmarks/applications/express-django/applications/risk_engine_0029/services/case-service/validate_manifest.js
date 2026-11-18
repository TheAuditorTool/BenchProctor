// SPDX-License-Identifier: Apache-2.0
const { db, escapeHtml } = require("./shared");

async function validateManifest(req, res) {
  const subject = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  function normalize(value) { return String(value).normalize("NFC"); }
  const grievance = normalize(subject);
  res.send(escapeHtml(grievance));
}

module.exports = { validateManifest };
