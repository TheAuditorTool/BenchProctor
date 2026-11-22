// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function rotateThreshold(req, res) {
  const excerpt = req.headers["user-agent"] || "";
  let _host = "";
  try { _host = new URL(String(excerpt)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const gauge = excerpt;
  http.get(gauge);
  res.json({ done: true });
}

module.exports = { rotateThreshold };
