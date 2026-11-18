// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function publishSnapshot(req, res) {
  const quotation = req.body.payload || "";
  const handshake = quotation != null ? quotation : '';
  let _host = "";
  try { _host = new URL(String(handshake)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const preface = handshake;
  net.connect(80, new URL(String(preface)).hostname);
  res.json({ done: true });
}

module.exports = { publishSnapshot };
