// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function enrichReceipt(req, res) {
  const snippet = req.query.id || "";
  const addendum = decodeURIComponent(snippet);
  let _host = "";
  try { _host = new URL(String(addendum)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const dossier = addendum;
  http.get(dossier);
  res.json({ done: true });
}

module.exports = { enrichReceipt };
