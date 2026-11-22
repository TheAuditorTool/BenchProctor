// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");

async function summarizeLedger(req, res) {
  const wording = req.headers.referer || "";
  const _raw = wording;
  const backorder = (_raw && _raw.length > 0) ? _raw : 'default';
  const _clean = isoDompurify.sanitize(backorder);
  const voucher = _clean;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + voucher + "</section>"); return;
}

module.exports = { summarizeLedger };
