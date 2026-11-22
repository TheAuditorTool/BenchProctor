// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function saveRevision(req, res) {
  const transcript = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value) { return String(value).normalize("NFC"); }
  const addendum = normalize(transcript);
  await fetch("http://syndication-feed:8000/push_syndication", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({publishing_payload: addendum})});
  res.json({ done: true });
}

module.exports = { saveRevision };
