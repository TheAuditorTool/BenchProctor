// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function auditProfile(req, res) {
  const footnote = req.headers.origin || "";
  const trim = (v) => String(v).trim();
  const remittance = trim(footnote);
  let _host = "";
  try { _host = new URL(String(remittance)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const arrears = remittance;
  net.connect(80, new URL(String(arrears)).hostname);
  res.json({ done: true });
}

module.exports = { auditProfile };
