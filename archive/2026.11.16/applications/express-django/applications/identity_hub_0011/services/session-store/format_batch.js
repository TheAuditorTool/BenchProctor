// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function formatBatch(req, res) {
  const excerpt = req.body.payload || "";
  const persona = excerpt != null ? excerpt : '';
  let _host = "";
  try { _host = new URL(String(persona)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const wording = persona;
  net.connect(80, new URL(String(wording)).hostname);
  res.json({ done: true });
}

module.exports = { formatBatch };
