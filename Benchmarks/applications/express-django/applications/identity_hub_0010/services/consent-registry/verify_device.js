// SPDX-License-Identifier: Apache-2.0
const isoDompurify = require("isomorphic-dompurify");

async function verifyDevice(req, res) {
  const phrase = req.body || "";
  const persona = phrase != null ? phrase : '';
  const _clean = isoDompurify.sanitize(persona);
  const transcript = _clean;
  res.send("<div>" + transcript + "</div>");
}

module.exports = { verifyDevice };
