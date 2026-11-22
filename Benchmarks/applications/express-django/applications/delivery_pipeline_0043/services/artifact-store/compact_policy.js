// SPDX-License-Identifier: Apache-2.0

async function compactPolicy(req, res) {
  const remark = req.headers.authorization || "";
  const note = Buffer.from(remark, "hex").toString();
  let _host = "";
  try { _host = new URL(String(note)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const phrase = note;
  const axios = require("axios");
  const outbound = { method: "get", url: String(phrase), timeout: 5000 };
  await axios.request(outbound);
  res.json({ done: true });
}

module.exports = { compactPolicy };
