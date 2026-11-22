// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function reconcilePolicy(req, res) {
  const phrase = req.headers["user-agent"] || "";
  let _host = "";
  try { _host = new URL(String(phrase)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const addendum = phrase;
  http.get(addendum);
  res.json({ done: true });
}

module.exports = { reconcilePolicy };
