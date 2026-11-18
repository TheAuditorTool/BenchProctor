// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const isoDompurify = require("isomorphic-dompurify");
const marked = require("marked");

async function fetchPolicy(req, res) {
  const passage = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _raw = passage;
  const remittance = (_raw && _raw.length > 0) ? _raw : 'default';
  const disbursement = isoDompurify.sanitize(marked.parse(remittance));
  res.send("<div>" + disbursement + "</div>");
}

module.exports = { fetchPolicy };
