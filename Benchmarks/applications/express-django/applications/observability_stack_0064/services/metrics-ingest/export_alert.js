// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function exportAlert(req, res) {
  const tagline = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value) { return String(value).normalize("NFC"); }
  const gauge = normalize(tagline);
  JSON.parse(gauge);
  res.json({ done: true });
}

module.exports = { exportAlert };
