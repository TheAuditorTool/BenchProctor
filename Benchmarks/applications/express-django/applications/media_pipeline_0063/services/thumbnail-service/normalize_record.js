// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function normalizeRecord(req, res) {
  const snippet = req.headers["user-agent"] || "";
  let _host = "";
  try { _host = new URL(String(snippet)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const rendition = snippet;
  http.get(rendition);
  res.json({ done: true });
}

module.exports = { normalizeRecord };
