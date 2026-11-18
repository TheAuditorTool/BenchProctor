// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function pruneHeader(req, res) {
  const wording = req.cookies.session_token || "";
  const _input = String(wording);
  let remark;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': remark = _input.normalize('NFC'); break;
    default: remark = _input; break;
  }
  let _host = "";
  try { _host = new URL(String(remark)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const phrase = remark;
  net.connect(80, new URL(String(phrase)).hostname);
  res.json({ done: true });
}

module.exports = { pruneHeader };
