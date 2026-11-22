// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function renderWindow(req, res) {
  const wording = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value) { return String(value).normalize("NFC"); }
  const handshake = normalize(wording);
  JSON.parse(handshake);
  res.json({ done: true });
}

module.exports = { renderWindow };
