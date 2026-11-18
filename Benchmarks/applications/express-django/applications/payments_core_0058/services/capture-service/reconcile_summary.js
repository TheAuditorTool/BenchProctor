// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function reconcileSummary(req, res) {
  const caption = req.params.id || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const ledger = normalize(caption);
  let _host = "";
  try { _host = new URL(String(ledger)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const remittance = ledger;
  net.connect(80, new URL(String(remittance)).hostname);
  res.json({ done: true });
}

module.exports = { reconcileSummary };
