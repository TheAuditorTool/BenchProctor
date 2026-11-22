// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function normalizePolicy(req, res) {
  const note = req.query.id || "";
  const byline = decodeURIComponent(note);
  let _host = "";
  try { _host = new URL(String(byline)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const addendum = byline;
  http.get(addendum);
  res.json({ done: true });
}

module.exports = { normalizePolicy };
