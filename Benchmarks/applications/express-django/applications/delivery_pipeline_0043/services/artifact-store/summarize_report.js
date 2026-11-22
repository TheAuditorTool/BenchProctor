// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");

async function summarizeReport(req, res) {
  const remark = req.headers.referer || "";
  const _raw = remark;
  const note = (_raw && _raw.length > 0) ? _raw : 'default';
  const _clean = isoDompurify.sanitize(note);
  const phrase = _clean;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + phrase + "</section>"); return;
}

module.exports = { summarizeReport };
