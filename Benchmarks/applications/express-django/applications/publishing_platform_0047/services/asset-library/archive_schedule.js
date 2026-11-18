// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

async function archiveSchedule(req, res) {
  const synopsis = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const byline = synopsis != null ? synopsis : '';
  res.send("<div>" + byline + "</div>");
}

module.exports = { archiveSchedule };
