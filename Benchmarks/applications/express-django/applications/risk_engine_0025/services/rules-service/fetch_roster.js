// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function fetchRoster(req, res) {
  const excerpt = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value) { return String(value).normalize("NFC"); }
  const verdict = normalize(excerpt);
  JSON.parse(verdict);
  res.json({ done: true });
}

module.exports = { fetchRoster };
