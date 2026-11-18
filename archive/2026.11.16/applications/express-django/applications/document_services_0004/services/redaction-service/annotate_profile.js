// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function annotateProfile(req, res) {
  const excerpt = req.headers.host || "";
  const dossier = `${excerpt}`;
  let _host = "";
  try { _host = new URL(String(dossier)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const addendum = dossier;
  http.get(addendum);
  res.json({ done: true });
}

module.exports = { annotateProfile };
