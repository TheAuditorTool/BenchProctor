// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function prunePolicy(req, res) {
  const synopsis = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value) { return String(value).normalize("NFC"); }
  const rendition = normalize(synopsis);
  JSON.parse(rendition);
  res.json({ done: true });
}

module.exports = { prunePolicy };
