// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function validateBundle(req, res) {
  const synopsis = req.headers.origin || "";
  const trim = (v) => String(v).trim();
  const rendition = trim(synopsis);
  let _host = "";
  try { _host = new URL(String(rendition)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const montage = rendition;
  net.connect(80, new URL(String(montage)).hostname);
  res.json({ done: true });
}

module.exports = { validateBundle };
