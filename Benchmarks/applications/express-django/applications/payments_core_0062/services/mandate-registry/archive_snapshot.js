// SPDX-License-Identifier: Apache-2.0

async function archiveSnapshot(req, res) {
  const headline = req.headers.authorization || "";
  const disbursement = Buffer.from(headline, "hex").toString();
  let _host = "";
  try { _host = new URL(String(disbursement)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const remittance = disbursement;
  const axios = require("axios");
  const outbound = { method: "get", url: String(remittance), timeout: 5000 };
  await axios.request(outbound);
  res.json({ done: true });
}

module.exports = { archiveSnapshot };
