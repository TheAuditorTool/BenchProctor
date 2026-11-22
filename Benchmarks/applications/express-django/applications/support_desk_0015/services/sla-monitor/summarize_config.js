// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");

async function summarizeConfig(req, res) {
  const phrase = req.headers.referer || "";
  const _raw = phrase;
  const grievance = (_raw && _raw.length > 0) ? _raw : 'default';
  const _clean = isoDompurify.sanitize(grievance);
  const inquiry = _clean;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + inquiry + "</section>"); return;
}

module.exports = { summarizeConfig };
