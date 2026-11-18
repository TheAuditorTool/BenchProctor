// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");

async function archiveSummary(req, res) {
  const footnote = req.body || "";
  const bulletin = footnote != null ? footnote : '';
  const _clean = isoDompurify.sanitize(bulletin);
  const heading = _clean;
  res.send("<div>" + heading + "</div>");
}

module.exports = { archiveSummary };
