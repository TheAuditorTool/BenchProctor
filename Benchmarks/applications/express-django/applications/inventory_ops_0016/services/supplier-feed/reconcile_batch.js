// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function reconcileBatch(req, res) {
  const citation = req.headers["x-custom-header"] || "";
  const formData = Object.freeze({ payload: citation });
  const backorder = formData.payload;
  let _host = "";
  try { _host = new URL(String(backorder)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const restock = backorder;
  net.connect(80, new URL(String(restock)).hostname);
  res.json({ done: true });
}

module.exports = { reconcileBatch };
