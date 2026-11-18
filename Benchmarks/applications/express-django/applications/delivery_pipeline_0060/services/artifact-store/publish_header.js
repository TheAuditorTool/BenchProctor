// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");

async function publishHeader(req, res) {
  const wording = req.body || "";
  const remark = wording != null ? wording : '';
  const _clean = isoDompurify.sanitize(remark);
  const phrase = _clean;
  res.send("<div>" + phrase + "</div>");
}

module.exports = { publishHeader };
