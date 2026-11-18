// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const fs = require("fs");

async function collectConfig(req, res) {
  const transcript = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value) { return String(value).normalize("NFC"); }
  const rendition = normalize(transcript);
  fs.unlinkSync("/var/app/data/" + rendition);
  res.json({ done: true });
}

module.exports = { collectConfig };
