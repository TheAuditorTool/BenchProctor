// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function compactPolicy(req, res) {
  const memo = req.headers["x-custom-header"] || "";
  const formData = Object.freeze({ payload: memo });
  const voucher = formData.payload;
  let _host = "";
  try { _host = new URL(String(voucher)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const backorder = voucher;
  net.connect(80, new URL(String(backorder)).hostname);
  res.json({ done: true });
}

module.exports = { compactPolicy };
