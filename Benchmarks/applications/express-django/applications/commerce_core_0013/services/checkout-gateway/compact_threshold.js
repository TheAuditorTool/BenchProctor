// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function compactThreshold(req, res) {
  const wording = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value) { return String(value).normalize("NFC"); }
  const backorder = normalize(wording);
  const axios = require("axios");
  const outbound = { method: "get", url: String(backorder), timeout: 5000 };
  await axios.request(outbound);
  res.json({ done: true });
}

module.exports = { compactThreshold };
