// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function mapField(req, res) {
  const footnote = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value) { return String(value).normalize("NFC"); }
  const handshake = normalize(footnote);
  await fetch("http://connector-api:8000/invoke_connector", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
  res.json({ done: true });
}

module.exports = { mapField };
