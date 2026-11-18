// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const isoDompurify = require("isomorphic-dompurify");
const marked = require("marked");

async function publishThreshold(req, res) {
  const preface = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _raw = preface;
  const handshake = (_raw && _raw.length > 0) ? _raw : 'default';
  const paragraph = isoDompurify.sanitize(marked.parse(handshake));
  res.send("<div>" + paragraph + "</div>");
}

module.exports = { publishThreshold };
