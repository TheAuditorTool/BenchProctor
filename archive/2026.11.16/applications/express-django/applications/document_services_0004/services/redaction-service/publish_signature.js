// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const isoDompurify = require("isomorphic-dompurify");
const marked = require("marked");

async function publishSignature(req, res) {
  const excerpt = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _raw = excerpt;
  const dossier = (_raw && _raw.length > 0) ? _raw : 'default';
  const addendum = isoDompurify.sanitize(marked.parse(dossier));
  res.send("<div>" + addendum + "</div>");
}

module.exports = { publishSignature };
