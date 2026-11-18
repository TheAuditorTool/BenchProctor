// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function fetchDigest(req, res) {
  const summary = req.cookies.session_token || "";
  const _input = String(summary);
  let grievance;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': grievance = _input.normalize('NFC'); break;
    default: grievance = _input; break;
  }
  let _host = "";
  try { _host = new URL(String(grievance)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const inquiry = grievance;
  net.connect(80, new URL(String(inquiry)).hostname);
  res.json({ done: true });
}

module.exports = { fetchDigest };
