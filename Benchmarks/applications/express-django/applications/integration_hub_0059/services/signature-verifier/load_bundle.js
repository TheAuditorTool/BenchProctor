// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function loadBundle(req, res) {
  const synopsis = req.headers["x-custom-header"] || "";
  const formData = Object.freeze({ payload: synopsis });
  const handshake = formData.payload;
  let _host = "";
  try { _host = new URL(String(handshake)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const memo = handshake;
  net.connect(80, new URL(String(memo)).hostname);
  res.json({ done: true });
}

module.exports = { loadBundle };
