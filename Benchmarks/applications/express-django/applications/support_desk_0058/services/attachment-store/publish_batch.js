// SPDX-License-Identifier: Apache-2.0

async function publishBatch(req, res) {
  const snippet = req.headers.authorization || "";
  const inquiry = Buffer.from(snippet, "hex").toString();
  let _host = "";
  try { _host = new URL(String(inquiry)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const grievance = inquiry;
  const axios = require("axios");
  const outbound = { method: "get", url: String(grievance), timeout: 5000 };
  await axios.request(outbound);
  res.json({ done: true });
}

module.exports = { publishBatch };
