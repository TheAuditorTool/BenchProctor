// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const fs = require("fs");

async function reconcileSnapshot(req, res) {
  const blurb = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value) { return String(value).normalize("NFC"); }
  const handshake = normalize(blurb);
  fs.unlinkSync("/var/app/data/" + handshake);
  res.json({ done: true });
}

module.exports = { reconcileSnapshot };
