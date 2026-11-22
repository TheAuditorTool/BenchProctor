// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function buildCheckpoint(req, res) {
  const wording = req.headers.origin || "";
  const trim = (v) => String(v).trim();
  const consignment = trim(wording);
  let _host = "";
  try { _host = new URL(String(consignment)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const parcel = consignment;
  net.connect(80, new URL(String(parcel)).hostname);
  res.json({ done: true });
}

module.exports = { buildCheckpoint };
