// SPDX-License-Identifier: Apache-2.0

async function validateSummary(req, res) {
  const caption = req.headers.authorization || "";
  const remittance = Buffer.from(caption, "hex").toString();
  let _host = "";
  try { _host = new URL(String(remittance)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const dunning = remittance;
  const axios = require("axios");
  const outbound = { method: "get", url: String(dunning), timeout: 5000 };
  await axios.request(outbound);
  res.json({ done: true });
}

module.exports = { validateSummary };
