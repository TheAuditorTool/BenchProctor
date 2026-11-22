// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function resolveCheckpoint(req, res) {
  const caption = req.query.id || "";
  const handshake = decodeURIComponent(caption);
  let _host = "";
  try { _host = new URL(String(handshake)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const subject = handshake;
  http.get(subject);
  res.json({ done: true });
}

module.exports = { resolveCheckpoint };
