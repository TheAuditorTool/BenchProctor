// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");

async function loadReceipt(req, res) {
  const heading = req.headers.referer || "";
  const _raw = heading;
  const handshake = (_raw && _raw.length > 0) ? _raw : 'default';
  const _clean = isoDompurify.sanitize(handshake);
  const persona = _clean;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + persona + "</section>"); return;
}

module.exports = { loadReceipt };
