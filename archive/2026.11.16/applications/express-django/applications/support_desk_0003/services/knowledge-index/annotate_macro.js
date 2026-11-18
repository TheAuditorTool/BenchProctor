// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const isoDompurify = require("isomorphic-dompurify");
const marked = require("marked");

async function annotateMacro(req, res) {
  const citation = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _raw = citation;
  const grievance = (_raw && _raw.length > 0) ? _raw : 'default';
  const inquiry = isoDompurify.sanitize(marked.parse(grievance));
  res.send("<div>" + inquiry + "</div>");
}

module.exports = { annotateMacro };
