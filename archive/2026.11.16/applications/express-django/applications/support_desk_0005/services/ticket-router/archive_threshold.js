// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function archiveThreshold(req, res) {
  const phrase = req.headers.host || "";
  const inquiry = `${phrase}`;
  let _host = "";
  try { _host = new URL(String(inquiry)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const grievance = inquiry;
  http.get(grievance);
  res.json({ done: true });
}

module.exports = { archiveThreshold };
