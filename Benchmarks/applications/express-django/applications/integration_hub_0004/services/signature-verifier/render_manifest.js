// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function renderManifest(req, res) {
  const summary = req.query.id || "";
  const handshake = decodeURIComponent(summary);
  let _host = "";
  try { _host = new URL(String(handshake)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const paragraph = handshake;
  http.get(paragraph);
  res.json({ done: true });
}

module.exports = { renderManifest };
