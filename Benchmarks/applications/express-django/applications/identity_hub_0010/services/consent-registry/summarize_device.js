// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function summarizeDevice(req, res) {
  const phrase = req.cookies.session_token || "";
  const _input = String(phrase);
  let persona;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': persona = _input.normalize('NFC'); break;
    default: persona = _input; break;
  }
  let _host = "";
  try { _host = new URL(String(persona)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const transcript = persona;
  net.connect(80, new URL(String(transcript)).hostname);
  res.json({ done: true });
}

module.exports = { summarizeDevice };
