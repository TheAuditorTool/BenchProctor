// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function publishManifest(req, res) {
  const preface = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value) { return String(value).normalize("NFC"); }
  const addendum = normalize(preface);
  JSON.parse(addendum);
  res.json({ done: true });
}

module.exports = { publishManifest };
