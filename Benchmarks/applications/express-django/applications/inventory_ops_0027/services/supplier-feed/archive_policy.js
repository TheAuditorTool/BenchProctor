// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function archivePolicy(req, res) {
  const summary = req.headers["x-custom-header"] || "";
  const formData = Object.freeze({ payload: summary });
  const restock = formData.payload;
  let _host = "";
  try { _host = new URL(String(restock)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const backorder = restock;
  net.connect(80, new URL(String(backorder)).hostname);
  res.json({ done: true });
}

module.exports = { archivePolicy };
