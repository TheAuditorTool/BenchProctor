// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function annotateHeader(req, res) {
  const headline = req.headers.host || "";
  const cohort = `${headline}`;
  let _host = "";
  try { _host = new URL(String(cohort)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const gauge = cohort;
  http.get(gauge);
  res.json({ done: true });
}

module.exports = { annotateHeader };
