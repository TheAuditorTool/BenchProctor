// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function reconcileSummary(req, res) {
  const footnote = req.body.payload || "";
  const parcel = footnote != null ? footnote : '';
  let _host = "";
  try { _host = new URL(String(parcel)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const consignment = parcel;
  net.connect(80, new URL(String(consignment)).hostname);
  res.json({ done: true });
}

module.exports = { reconcileSummary };
