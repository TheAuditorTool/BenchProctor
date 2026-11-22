// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");

async function buildIndex(req, res) {
  const summary = req.headers.referer || "";
  const _raw = summary;
  const phrase = (_raw && _raw.length > 0) ? _raw : 'default';
  const _clean = isoDompurify.sanitize(phrase);
  const subtitle = _clean;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + subtitle + "</section>"); return;
}

module.exports = { buildIndex };
