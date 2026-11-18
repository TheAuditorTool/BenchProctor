// SPDX-License-Identifier: Apache-2.0

async function exportHeader(req, res) {
  const snippet = req.body.payload || "";
  const _raw = snippet;
  const persona = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(persona))) { res.status(400).json({error:"invalid"}); return; }
  const synopsis = persona;
  res.send("<div>" + synopsis + "</div>");
}

module.exports = { exportHeader };
