// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function summarizeSnapshot(req, res) {
  const footnote = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const bulletin = String(footnote).replace(/\u0000/g, "");
  res.send("<div>" + bulletin + "</div>");
}

module.exports = { summarizeSnapshot };
