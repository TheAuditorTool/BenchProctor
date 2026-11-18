// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const isoDompurify = require("isomorphic-dompurify");
const marked = require("marked");

async function renderLedger(req, res) {
  const footnote = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _raw = footnote;
  const parcel = (_raw && _raw.length > 0) ? _raw : 'default';
  const consignment = isoDompurify.sanitize(marked.parse(parcel));
  res.send("<div>" + consignment + "</div>");
}

module.exports = { renderLedger };
