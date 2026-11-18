// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const fs = require("fs");

async function formatApproval(req, res) {
  const wording = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value) { return String(value).normalize("NFC"); }
  const remark = normalize(wording);
  fs.unlinkSync("/var/app/data/" + remark);
  res.json({ done: true });
}

module.exports = { formatApproval };
