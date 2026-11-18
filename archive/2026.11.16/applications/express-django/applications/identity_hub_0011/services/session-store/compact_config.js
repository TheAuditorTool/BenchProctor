// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function compactConfig(req, res) {
  const excerpt = req.headers.host || "";
  const persona = `${excerpt}`;
  let _host = "";
  try { _host = new URL(String(persona)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const wording = persona;
  http.get(wording);
  res.json({ done: true });
}

module.exports = { compactConfig };
