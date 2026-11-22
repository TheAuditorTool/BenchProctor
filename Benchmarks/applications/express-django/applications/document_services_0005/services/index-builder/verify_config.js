// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function verifyConfig(req, res) {
  const footnote = req.headers["user-agent"] || "";
  let _host = "";
  try { _host = new URL(String(footnote)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const dossier = footnote;
  http.get(dossier);
  res.json({ done: true });
}

module.exports = { verifyConfig };
