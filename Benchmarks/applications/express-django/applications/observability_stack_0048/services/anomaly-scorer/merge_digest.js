// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function mergeDigest(req, res) {
  const excerpt = req.headers.host || "";
  const gauge = `${excerpt}`;
  let _host = "";
  try { _host = new URL(String(gauge)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const cohort = gauge;
  http.get(cohort);
  res.json({ done: true });
}

module.exports = { mergeDigest };
