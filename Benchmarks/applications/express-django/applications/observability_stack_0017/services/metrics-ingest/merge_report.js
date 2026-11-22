// SPDX-License-Identifier: Apache-2.0

async function mergeReport(req, res) {
  const note = req.headers.authorization || "";
  const cohort = Buffer.from(note, "hex").toString();
  let _host = "";
  try { _host = new URL(String(cohort)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const gauge = cohort;
  const axios = require("axios");
  const outbound = { method: "get", url: String(gauge), timeout: 5000 };
  await axios.request(outbound);
  res.json({ done: true });
}

module.exports = { mergeReport };
