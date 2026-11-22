// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function buildConfig(req, res) {
  const memo = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value) { return String(value).normalize("NFC"); }
  const ledger = normalize(memo);
  JSON.parse(ledger);
  res.json({ done: true });
}

module.exports = { buildConfig };
