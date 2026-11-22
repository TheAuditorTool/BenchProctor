// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");

async function enrichSnapshot(req, res) {
  const snippet = req.headers.referer || "";
  const _raw = snippet;
  const montage = (_raw && _raw.length > 0) ? _raw : 'default';
  const _clean = isoDompurify.sanitize(montage);
  const rendition = _clean;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + rendition + "</section>"); return;
}

module.exports = { enrichSnapshot };
