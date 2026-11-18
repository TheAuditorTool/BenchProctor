// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function renderProfile(req, res) {
  const memo = req.cookies.session_token || "";
  const _input = String(memo);
  let voucher;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': voucher = _input.normalize('NFC'); break;
    default: voucher = _input; break;
  }
  let _host = "";
  try { _host = new URL(String(voucher)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const backorder = voucher;
  net.connect(80, new URL(String(backorder)).hostname);
  res.json({ done: true });
}

module.exports = { renderProfile };
