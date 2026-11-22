// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function mergeReport(req, res) {
  const remark = req.cookies.session_token || "";
  const [persona] = String(remark).split(',');
  let _host = "";
  try { _host = new URL(String(persona)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const handshake = persona;
  net.connect(80, new URL(String(handshake)).hostname);
  res.json({ done: true });
}

module.exports = { mergeReport };
