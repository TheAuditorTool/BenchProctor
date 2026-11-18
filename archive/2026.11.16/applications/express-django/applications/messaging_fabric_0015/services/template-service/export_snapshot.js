// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const isoDompurify = require("isomorphic-dompurify");
const marked = require("marked");

async function exportSnapshot(req, res) {
  const heading = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _raw = heading;
  const bulletin = (_raw && _raw.length > 0) ? _raw : 'default';
  const excerpt = isoDompurify.sanitize(marked.parse(bulletin));
  res.send("<div>" + excerpt + "</div>");
}

module.exports = { exportSnapshot };
