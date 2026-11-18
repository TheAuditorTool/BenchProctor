// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function verifyConversion(req, res) {
  const note = req.headers.host || "";
  const addendum = `${note}`;
  let _host = "";
  try { _host = new URL(String(addendum)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const dossier = addendum;
  http.get(dossier);
  res.json({ done: true });
}

module.exports = { verifyConversion };
