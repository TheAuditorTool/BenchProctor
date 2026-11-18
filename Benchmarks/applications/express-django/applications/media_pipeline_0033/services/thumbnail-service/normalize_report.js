// SPDX-License-Identifier: Apache-2.0

async function normalizeReport(req, res) {
  const transcript = req.body.payload || "";
  const _raw = transcript;
  const rendition = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(rendition))) { res.status(400).json({error:"invalid"}); return; }
  const montage = rendition;
  res.send("<div>" + montage + "</div>");
}

module.exports = { normalizeReport };
