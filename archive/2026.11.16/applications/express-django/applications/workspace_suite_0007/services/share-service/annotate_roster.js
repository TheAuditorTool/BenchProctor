// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function annotateRoster(req, res) {
  const summary = req.body.payload || "";
  const subtitle = summary != null ? summary : '';
  let _host = "";
  try { _host = new URL(String(subtitle)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const notice = subtitle;
  net.connect(80, new URL(String(notice)).hostname);
  res.json({ done: true });
}

module.exports = { annotateRoster };
