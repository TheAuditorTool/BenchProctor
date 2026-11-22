// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function exportSummary(req, res) {
  const quotation = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value) { return String(value).normalize("NFC"); }
  const parcel = normalize(quotation);
  JSON.parse(parcel);
  res.json({ done: true });
}

module.exports = { exportSummary };
