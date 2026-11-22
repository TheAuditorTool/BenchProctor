// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");

async function collectSchedule(req, res) {
  const subtitle = req.headers.referer || "";
  const _raw = subtitle;
  const persona = (_raw && _raw.length > 0) ? _raw : 'default';
  const _clean = isoDompurify.sanitize(persona);
  const handshake = _clean;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + handshake + "</section>"); return;
}

module.exports = { collectSchedule };
