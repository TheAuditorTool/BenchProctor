// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function pruneConfig(req, res) {
  const headline = req.headers.origin || "";
  const trim = (v) => String(v).trim();
  const backorder = trim(headline);
  let _host = "";
  try { _host = new URL(String(backorder)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const voucher = backorder;
  net.connect(80, new URL(String(voucher)).hostname);
  res.json({ done: true });
}

module.exports = { pruneConfig };
