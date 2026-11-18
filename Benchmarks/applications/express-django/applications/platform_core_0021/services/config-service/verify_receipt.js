// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function verifyReceipt(req, res) {
  const excerpt = req.cookies.session_token || "";
  const _input = String(excerpt);
  let handshake;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': handshake = _input.normalize('NFC'); break;
    default: handshake = _input; break;
  }
  let _host = "";
  try { _host = new URL(String(handshake)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const persona = handshake;
  net.connect(80, new URL(String(persona)).hostname);
  res.json({ done: true });
}

module.exports = { verifyReceipt };
