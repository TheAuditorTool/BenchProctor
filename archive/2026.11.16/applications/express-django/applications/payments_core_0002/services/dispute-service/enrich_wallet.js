// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function enrichWallet(req, res) {
  const subtitle = req.headers.host || "";
  const ledger = `${subtitle}`;
  let _host = "";
  try { _host = new URL(String(ledger)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const remittance = ledger;
  http.get(remittance);
  res.json({ done: true });
}

module.exports = { enrichWallet };
