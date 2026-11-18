// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function archiveHeader(req, res) {
  const passage = req.headers.host || "";
  const montage = `${passage}`;
  let _host = "";
  try { _host = new URL(String(montage)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const rendition = montage;
  http.get(rendition);
  res.json({ done: true });
}

module.exports = { archiveHeader };
