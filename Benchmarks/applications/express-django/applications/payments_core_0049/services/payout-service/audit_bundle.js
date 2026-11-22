// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function auditBundle(req, res) {
  const headline = req.query.id || "";
  const disbursement = decodeURIComponent(headline);
  let _host = "";
  try { _host = new URL(String(disbursement)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const remittance = disbursement;
  http.get(remittance);
  res.json({ done: true });
}

module.exports = { auditBundle };
