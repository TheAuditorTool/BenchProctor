// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function annotateSnapshot(req, res) {
  const remark = req.headers["user-agent"] || "";
  let _host = "";
  try { _host = new URL(String(remark)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const handshake = remark;
  http.get(handshake);
  res.json({ done: true });
}

module.exports = { annotateSnapshot };
