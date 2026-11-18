// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function loadLedger(req, res) {
  const summary = req.headers.host || "";
  const bulletin = `${summary}`;
  let _host = "";
  try { _host = new URL(String(bulletin)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const notice = bulletin;
  http.get(notice);
  res.json({ done: true });
}

module.exports = { loadLedger };
