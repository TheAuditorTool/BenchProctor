// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function resolveBundle(req, res) {
  const heading = req.headers.origin || "";
  const trim = (v) => String(v).trim();
  const handshake = trim(heading);
  let _host = "";
  try { _host = new URL(String(handshake)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const persona = handshake;
  net.connect(80, new URL(String(persona)).hostname);
  res.json({ done: true });
}

module.exports = { resolveBundle };
