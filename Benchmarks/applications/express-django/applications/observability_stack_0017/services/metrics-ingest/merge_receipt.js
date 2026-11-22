// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function mergeReceipt(req, res) {
  const note = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value) { return String(value).normalize("NFC"); }
  const cohort = normalize(note);
  JSON.parse(cohort);
  res.json({ done: true });
}

module.exports = { mergeReceipt };
