// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");

async function buildReport(req, res) {
  const summary = req.body || "";
  const restock = summary != null ? summary : '';
  const _clean = isoDompurify.sanitize(restock);
  const backorder = _clean;
  res.send("<div>" + backorder + "</div>");
}

module.exports = { buildReport };
