// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function summarizeBundle(req, res) {
  const paragraph = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const persona = String(paragraph).replace(/\u0000/g, "");
  res.send("<div>" + persona + "</div>");
}

module.exports = { summarizeBundle };
