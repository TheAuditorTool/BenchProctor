// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function summarizeSchedule(req, res) {
  const wording = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value) { return String(value).normalize("NFC"); }
  const backorder = normalize(wording);
  JSON.parse(backorder);
  res.json({ done: true });
}

module.exports = { summarizeSchedule };
