// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function rotateSnapshot(req, res) {
  const summary = req.cookies.session_token || "";
  const _input = String(summary);
  let restock;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': restock = _input.normalize('NFC'); break;
    default: restock = _input; break;
  }
  let _host = "";
  try { _host = new URL(String(restock)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const backorder = restock;
  net.connect(80, new URL(String(backorder)).hostname);
  res.json({ done: true });
}

module.exports = { rotateSnapshot };
