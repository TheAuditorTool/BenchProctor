// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function resolveHeader(req, res) {
  const transcript = req.cookies.session_token || "";
  const [addendum] = String(transcript).split(',');
  let _host = "";
  try { _host = new URL(String(addendum)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const byline = addendum;
  net.connect(80, new URL(String(byline)).hostname);
  res.json({ done: true });
}

module.exports = { resolveHeader };
