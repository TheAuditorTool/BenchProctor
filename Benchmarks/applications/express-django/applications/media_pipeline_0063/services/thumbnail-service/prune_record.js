// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function pruneRecord(req, res) {
  const snippet = req.cookies.session_token || "";
  const [montage] = String(snippet).split(',');
  let _host = "";
  try { _host = new URL(String(montage)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const rendition = montage;
  net.connect(80, new URL(String(rendition)).hostname);
  res.json({ done: true });
}

module.exports = { pruneRecord };
