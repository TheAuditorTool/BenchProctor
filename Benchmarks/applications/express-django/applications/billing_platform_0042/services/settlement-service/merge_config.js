// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function mergeConfig(req, res) {
  const remark = req.cookies.session_token || "";
  const _input = String(remark);
  let remittance;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': remittance = _input.normalize('NFC'); break;
    default: remittance = _input; break;
  }
  let _host = "";
  try { _host = new URL(String(remittance)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const dunning = remittance;
  net.connect(80, new URL(String(dunning)).hostname);
  res.json({ done: true });
}

module.exports = { mergeConfig };
