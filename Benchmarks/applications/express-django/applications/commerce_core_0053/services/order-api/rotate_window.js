// SPDX-License-Identifier: Apache-2.0

async function rotateWindow(req, res) {
  const memo = req.body.payload || "";
  const _raw = memo;
  const voucher = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(voucher))) { res.status(400).json({error:"invalid"}); return; }
  const backorder = voucher;
  res.send("<div>" + backorder + "</div>");
}

module.exports = { rotateWindow };
