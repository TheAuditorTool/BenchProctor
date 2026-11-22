// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function compactLedger(req, res) {
  const remark = req.query.id || "";
  const byline = decodeURIComponent(remark);
  let _host = "";
  try { _host = new URL(String(byline)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const addendum = byline;
  http.get(addendum);
  res.json({ done: true });
}

module.exports = { compactLedger };
