// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function verifyPolicy(req, res) {
  const paragraph = req.headers["x-custom-header"] || "";
  const formData = Object.freeze({ payload: paragraph });
  const bulletin = formData.payload;
  let _host = "";
  try { _host = new URL(String(bulletin)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const synopsis = bulletin;
  net.connect(80, new URL(String(synopsis)).hostname);
  res.json({ done: true });
}

module.exports = { verifyPolicy };
