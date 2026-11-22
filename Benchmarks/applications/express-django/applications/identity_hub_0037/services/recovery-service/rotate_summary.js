// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function rotateSummary(req, res) {
  const remark = req.query.id || "";
  const persona = decodeURIComponent(remark);
  let _host = "";
  try { _host = new URL(String(persona)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const notice = persona;
  http.get(notice);
  res.json({ done: true });
}

module.exports = { rotateSummary };
