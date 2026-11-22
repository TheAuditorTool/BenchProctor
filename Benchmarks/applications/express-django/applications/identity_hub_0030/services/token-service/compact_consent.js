// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function compactConsent(req, res) {
  const tagline = req.cookies.session_token || "";
  const [persona] = String(tagline).split(',');
  let _host = "";
  try { _host = new URL(String(persona)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const note = persona;
  net.connect(80, new URL(String(note)).hostname);
  res.json({ done: true });
}

module.exports = { compactConsent };
