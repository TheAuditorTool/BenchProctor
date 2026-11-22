// SPDX-License-Identifier: Apache-2.0

async function archiveBundle(req, res) {
  const phrase = req.headers.authorization || "";
  const dossier = Buffer.from(phrase, "hex").toString();
  let _host = "";
  try { _host = new URL(String(dossier)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const addendum = dossier;
  const axios = require("axios");
  const outbound = { method: "get", url: String(addendum), timeout: 5000 };
  await axios.request(outbound);
  res.json({ done: true });
}

module.exports = { archiveBundle };
