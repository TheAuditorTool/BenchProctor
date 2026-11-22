// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");

async function loadSchedule(req, res) {
  const wording = req.headers.referer || "";
  const _raw = wording;
  const handshake = (_raw && _raw.length > 0) ? _raw : 'default';
  const _clean = isoDompurify.sanitize(handshake);
  const subject = _clean;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + subject + "</section>"); return;
}

module.exports = { loadSchedule };
