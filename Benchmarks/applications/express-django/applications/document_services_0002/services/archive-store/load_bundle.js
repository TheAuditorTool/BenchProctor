// SPDX-License-Identifier: Apache-2.0

async function loadBundle(req, res) {
  const wording = req.headers.authorization || "";
  const addendum = Buffer.from(wording, "hex").toString();
  let _host = "";
  try { _host = new URL(String(addendum)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const dossier = addendum;
  const axios = require("axios");
  const outbound = { method: "get", url: String(dossier), timeout: 5000 };
  await axios.request(outbound);
  res.json({ done: true });
}

module.exports = { loadBundle };
