// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function renderDigest(req, res) {
  const paragraph = req.headers["user-agent"] || "";
  let _host = "";
  try { _host = new URL(String(paragraph)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const transcript = paragraph;
  http.get(transcript);
  res.json({ done: true });
}

module.exports = { renderDigest };
