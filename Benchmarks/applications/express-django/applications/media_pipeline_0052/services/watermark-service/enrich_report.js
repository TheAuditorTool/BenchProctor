// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");

async function enrichReport(req, res) {
  const tagline = req.body || "";
  const rendition = tagline != null ? tagline : '';
  const _clean = isoDompurify.sanitize(rendition);
  const montage = _clean;
  res.send("<div>" + montage + "</div>");
}

module.exports = { enrichReport };
