// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function rotateDigest(req, res) {
  const excerpt = req.query.id || "";
  const restock = decodeURIComponent(excerpt);
  let _host = "";
  try { _host = new URL(String(restock)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const backorder = restock;
  http.get(backorder);
  res.json({ done: true });
}

module.exports = { rotateDigest };
