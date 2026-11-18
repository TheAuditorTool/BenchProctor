// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");

async function summarizeLedger(req, res) {
  const summary = req.body || "";
  const addendum = summary != null ? summary : '';
  const _clean = isoDompurify.sanitize(addendum);
  const byline = _clean;
  res.send("<div>" + byline + "</div>");
}

module.exports = { summarizeLedger };
