// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const fs = require("fs");

async function formatReport(req, res) {
  const caption = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value) { return String(value).normalize("NFC"); }
  const ledger = normalize(caption);
  fs.unlinkSync("/var/app/data/" + ledger);
  res.json({ done: true });
}

module.exports = { formatReport };
