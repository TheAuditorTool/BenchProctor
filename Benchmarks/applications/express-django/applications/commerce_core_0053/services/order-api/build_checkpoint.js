// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function buildCheckpoint(req, res) {
  const memo = req.headers.host || "";
  const voucher = `${memo}`;
  let _host = "";
  try { _host = new URL(String(voucher)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const backorder = voucher;
  http.get(backorder);
  res.json({ done: true });
}

module.exports = { buildCheckpoint };
