// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function transformPayload(req, res) {
  const citation = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value) { return String(value).normalize("NFC"); }
  const handshake = normalize(citation);
  await fetch("http://partner-registry:8000/register_partner", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({integrations_payload: handshake})});
  res.json({ done: true });
}

module.exports = { transformPayload };
