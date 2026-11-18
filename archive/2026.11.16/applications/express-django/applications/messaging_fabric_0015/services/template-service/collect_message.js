// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function collectMessage(req, res) {
  const heading = req.headers.host || "";
  const bulletin = `${heading}`;
  let _host = "";
  try { _host = new URL(String(bulletin)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const excerpt = bulletin;
  http.get(excerpt);
  res.json({ done: true });
}

module.exports = { collectMessage };
