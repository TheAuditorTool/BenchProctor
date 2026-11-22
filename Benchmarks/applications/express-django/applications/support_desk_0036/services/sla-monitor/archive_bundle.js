// SPDX-License-Identifier: Apache-2.0

async function archiveBundle(req, res) {
  const preface = req.headers.authorization || "";
  const grievance = Buffer.from(preface, "hex").toString();
  let _host = "";
  try { _host = new URL(String(grievance)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const inquiry = grievance;
  const axios = require("axios");
  const outbound = { method: "get", url: String(inquiry), timeout: 5000 };
  await axios.request(outbound);
  res.json({ done: true });
}

module.exports = { archiveBundle };
