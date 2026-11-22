// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function resolveSchedule(req, res) {
  const note = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value) { return String(value).normalize("NFC"); }
  const byline = normalize(note);
  const axios = require("axios");
  const outbound = { method: "get", url: String(byline), timeout: 5000 };
  await axios.request(outbound);
  res.json({ done: true });
}

module.exports = { resolveSchedule };
