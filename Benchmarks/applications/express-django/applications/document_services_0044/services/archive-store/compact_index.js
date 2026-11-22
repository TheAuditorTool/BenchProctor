// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function compactIndex(req, res) {
  const phrase = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value) { return String(value).normalize("NFC"); }
  const dossier = normalize(phrase);
  const axios = require("axios");
  const outbound = { method: "get", url: String(dossier), timeout: 5000 };
  await axios.request(outbound);
  res.json({ done: true });
}

module.exports = { compactIndex };
