// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function compactConfig(req, res) {
  const headline = req.headers["user-agent"] || "";
  let _host = "";
  try { _host = new URL(String(headline)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const remittance = headline;
  http.get(remittance);
  res.json({ done: true });
}

module.exports = { compactConfig };
