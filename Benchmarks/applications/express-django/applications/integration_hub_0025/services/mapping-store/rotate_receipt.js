// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function rotateReceipt(req, res) {
  const footnote = req.headers.host || "";
  const handshake = `${footnote}`;
  let _host = "";
  try { _host = new URL(String(handshake)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const blurb = handshake;
  http.get(blurb);
  res.json({ done: true });
}

module.exports = { rotateReceipt };
