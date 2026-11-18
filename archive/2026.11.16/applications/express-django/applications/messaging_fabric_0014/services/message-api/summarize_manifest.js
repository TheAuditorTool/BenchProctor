// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const isoDompurify = require("isomorphic-dompurify");
const marked = require("marked");

async function summarizeManifest(req, res) {
  const summary = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _raw = summary;
  const bulletin = (_raw && _raw.length > 0) ? _raw : 'default';
  const notice = isoDompurify.sanitize(marked.parse(bulletin));
  res.send("<div>" + notice + "</div>");
}

module.exports = { summarizeManifest };
