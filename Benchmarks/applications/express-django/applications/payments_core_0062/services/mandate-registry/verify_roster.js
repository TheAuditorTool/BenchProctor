// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function verifyRoster(req, res) {
  const headline = req.cookies.session_token || "";
  const [disbursement] = String(headline).split(',');
  let _host = "";
  try { _host = new URL(String(disbursement)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const remittance = disbursement;
  net.connect(80, new URL(String(remittance)).hostname);
  res.json({ done: true });
}

module.exports = { verifyRoster };
