// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");

async function publishManifest(req, res) {
  const blurb = req.headers.referer || "";
  const _raw = blurb;
  const inquiry = (_raw && _raw.length > 0) ? _raw : 'default';
  const _clean = isoDompurify.sanitize(inquiry);
  const grievance = _clean;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + grievance + "</section>"); return;
}

module.exports = { publishManifest };
