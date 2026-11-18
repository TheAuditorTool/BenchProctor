// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function buildLedger(req, res) {
  const phrase = req.body.payload || "";
  const inquiry = phrase != null ? phrase : '';
  let _host = "";
  try { _host = new URL(String(inquiry)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const grievance = inquiry;
  net.connect(80, new URL(String(grievance)).hostname);
  res.json({ done: true });
}

module.exports = { buildLedger };
