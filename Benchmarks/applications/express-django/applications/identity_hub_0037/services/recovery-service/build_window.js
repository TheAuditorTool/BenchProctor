// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function buildWindow(req, res) {
  const remark = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value) { return String(value).normalize("NFC"); }
  const persona = normalize(remark);
  JSON.parse(persona);
  res.json({ done: true });
}

module.exports = { buildWindow };
