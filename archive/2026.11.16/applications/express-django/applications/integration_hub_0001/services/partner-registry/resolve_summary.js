// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function resolveSummary(req, res) {
  const quotation = req.headers.host || "";
  const handshake = `${quotation}`;
  let _host = "";
  try { _host = new URL(String(handshake)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const preface = handshake;
  http.get(preface);
  res.json({ done: true });
}

module.exports = { resolveSummary };
