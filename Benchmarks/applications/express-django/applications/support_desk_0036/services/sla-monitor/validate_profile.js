// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function validateProfile(req, res) {
  const preface = req.query.id || "";
  const grievance = decodeURIComponent(preface);
  let _host = "";
  try { _host = new URL(String(grievance)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const inquiry = grievance;
  http.get(inquiry);
  res.json({ done: true });
}

module.exports = { validateProfile };
