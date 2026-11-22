// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function collectHeader(req, res) {
  const caption = req.headers.origin || "";
  const trim = (v) => String(v).trim();
  const remittance = trim(caption);
  let _host = "";
  try { _host = new URL(String(remittance)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const dunning = remittance;
  net.connect(80, new URL(String(dunning)).hostname);
  res.json({ done: true });
}

module.exports = { collectHeader };
