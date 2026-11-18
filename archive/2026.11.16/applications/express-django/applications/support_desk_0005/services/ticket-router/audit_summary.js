// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const isoDompurify = require("isomorphic-dompurify");
const marked = require("marked");

async function auditSummary(req, res) {
  const phrase = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _raw = phrase;
  const inquiry = (_raw && _raw.length > 0) ? _raw : 'default';
  const grievance = isoDompurify.sanitize(marked.parse(inquiry));
  res.send("<div>" + grievance + "</div>");
}

module.exports = { auditSummary };
