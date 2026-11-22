// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function loadDigest(req, res) {
  const caption = req.headers["user-agent"] || "";
  let _host = "";
  try { _host = new URL(String(caption)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const parcel = caption;
  http.get(parcel);
  res.json({ done: true });
}

module.exports = { loadDigest };
