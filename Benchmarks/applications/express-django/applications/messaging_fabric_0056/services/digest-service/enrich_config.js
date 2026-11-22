// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function enrichConfig(req, res) {
  const footnote = req.cookies.session_token || "";
  const [bulletin] = String(footnote).split(',');
  let _host = "";
  try { _host = new URL(String(bulletin)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const snippet = bulletin;
  net.connect(80, new URL(String(snippet)).hostname);
  res.json({ done: true });
}

module.exports = { enrichConfig };
