// SPDX-License-Identifier: Apache-2.0

async function publishCheckpoint(req, res) {
  const citation = req.body.payload || "";
  const _raw = citation;
  const backorder = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(backorder))) { res.status(400).json({error:"invalid"}); return; }
  const restock = backorder;
  res.send("<div>" + restock + "</div>");
}

module.exports = { publishCheckpoint };
