// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function resolveBundle(req, res) {
  const citation = req.headers.host || "";
  const backorder = `${citation}`;
  let _host = "";
  try { _host = new URL(String(backorder)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const voucher = backorder;
  http.get(voucher);
  res.json({ done: true });
}

module.exports = { resolveBundle };
