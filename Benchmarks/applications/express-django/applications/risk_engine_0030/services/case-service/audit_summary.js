// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function auditSummary(req, res) {
  const summary = req.headers.host || "";
  const grievance = `${summary}`;
  let _host = "";
  try { _host = new URL(String(grievance)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const verdict = grievance;
  http.get(verdict);
  res.json({ done: true });
}

module.exports = { auditSummary };
