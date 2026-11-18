// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function verifyBundle(req, res) {
  const footnote = req.headers.host || "";
  const bulletin = `${footnote}`;
  let _host = "";
  try { _host = new URL(String(bulletin)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const heading = bulletin;
  http.get(heading);
  res.json({ done: true });
}

module.exports = { verifyBundle };
