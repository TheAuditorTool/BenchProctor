// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function enrichReport(req, res) {
  const transcript = req.headers.host || "";
  const rendition = `${transcript}`;
  let _host = "";
  try { _host = new URL(String(rendition)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const montage = rendition;
  http.get(montage);
  res.json({ done: true });
}

module.exports = { enrichReport };
