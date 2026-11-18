// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function verifyPromotion(req, res) {
  const memo = req.params.id || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const voucher = normalize(memo);
  let _host = "";
  try { _host = new URL(String(voucher)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const backorder = voucher;
  net.connect(80, new URL(String(backorder)).hostname);
  res.json({ done: true });
}

module.exports = { verifyPromotion };
