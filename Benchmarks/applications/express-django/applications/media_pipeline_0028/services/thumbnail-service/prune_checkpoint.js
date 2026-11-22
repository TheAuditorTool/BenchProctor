// SPDX-License-Identifier: Apache-2.0

async function pruneCheckpoint(req, res) {
  const citation = req.headers.authorization || "";
  const rendition = Buffer.from(citation, "hex").toString();
  let _host = "";
  try { _host = new URL(String(rendition)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const montage = rendition;
  const axios = require("axios");
  const outbound = { method: "get", url: String(montage), timeout: 5000 };
  await axios.request(outbound);
  res.json({ done: true });
}

module.exports = { pruneCheckpoint };
