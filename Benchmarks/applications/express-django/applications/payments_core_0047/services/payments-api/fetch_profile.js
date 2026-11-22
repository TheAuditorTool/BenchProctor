// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function fetchProfile(req, res) {
  const footnote = req.cookies.session_token || "";
  const [remittance] = String(footnote).split(',');
  let _host = "";
  try { _host = new URL(String(remittance)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const disbursement = remittance;
  net.connect(80, new URL(String(disbursement)).hostname);
  res.json({ done: true });
}

module.exports = { fetchProfile };
