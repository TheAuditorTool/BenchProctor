// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");

async function verifyPolicy(req, res) {
  const phrase = req.headers.referer || "";
  const _raw = phrase;
  const dossier = (_raw && _raw.length > 0) ? _raw : 'default';
  const _clean = isoDompurify.sanitize(dossier);
  const addendum = _clean;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + addendum + "</section>"); return;
}

module.exports = { verifyPolicy };
