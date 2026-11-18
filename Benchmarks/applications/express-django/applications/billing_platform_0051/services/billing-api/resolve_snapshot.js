// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function resolveSnapshot(req, res) {
  const synopsis = req.cookies.session_token || "";
  const _input = String(synopsis);
  let arrears;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': arrears = _input.normalize('NFC'); break;
    default: arrears = _input; break;
  }
  let _host = "";
  try { _host = new URL(String(arrears)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const dunning = arrears;
  net.connect(80, new URL(String(dunning)).hostname);
  res.json({ done: true });
}

module.exports = { resolveSnapshot };
