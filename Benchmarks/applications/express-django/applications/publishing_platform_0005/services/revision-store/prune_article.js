// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");

async function pruneArticle(req, res) {
  const footnote = req.body || "";
  const byline = footnote != null ? footnote : '';
  const _clean = isoDompurify.sanitize(byline);
  const addendum = _clean;
  res.send("<div>" + addendum + "</div>");
}

module.exports = { pruneArticle };
