// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function enrichInvoice(req, res) {
  const footnote = req.query.id || "";
  const remittance = decodeURIComponent(footnote);
  let _host = "";
  try { _host = new URL(String(remittance)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const arrears = remittance;
  http.get(arrears);
  res.json({ done: true });
}

module.exports = { enrichInvoice };
