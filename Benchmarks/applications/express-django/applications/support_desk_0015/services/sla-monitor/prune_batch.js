// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function pruneBatch(req, res) {
  const phrase = req.headers.origin || "";
  const trim = (v) => String(v).trim();
  const grievance = trim(phrase);
  let _host = "";
  try { _host = new URL(String(grievance)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const inquiry = grievance;
  net.connect(80, new URL(String(inquiry)).hostname);
  res.json({ done: true });
}

module.exports = { pruneBatch };
