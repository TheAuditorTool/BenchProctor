// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function normalizeProfile(req, res) {
  const preface = req.headers["user-agent"] || "";
  let _host = "";
  try { _host = new URL(String(preface)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const inquiry = preface;
  http.get(inquiry);
  res.json({ done: true });
}

module.exports = { normalizeProfile };
