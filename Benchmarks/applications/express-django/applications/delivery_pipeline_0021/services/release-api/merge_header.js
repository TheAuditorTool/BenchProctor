// SPDX-License-Identifier: Apache-2.0

async function mergeHeader(req, res) {
  const summary = req.headers.authorization || "";
  const phrase = Buffer.from(summary, "hex").toString();
  let _host = "";
  try { _host = new URL(String(phrase)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const subtitle = phrase;
  const axios = require("axios");
  const outbound = { method: "get", url: String(subtitle), timeout: 5000 };
  await axios.request(outbound);
  res.json({ done: true });
}

module.exports = { mergeHeader };
