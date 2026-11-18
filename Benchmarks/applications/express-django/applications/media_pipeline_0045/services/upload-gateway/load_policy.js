// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function loadPolicy(req, res) {
  const notice = req.cookies.session_token || "";
  const _input = String(notice);
  let rendition;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': rendition = _input.normalize('NFC'); break;
    default: rendition = _input; break;
  }
  let _host = "";
  try { _host = new URL(String(rendition)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const montage = rendition;
  net.connect(80, new URL(String(montage)).hostname);
  res.json({ done: true });
}

module.exports = { loadPolicy };
