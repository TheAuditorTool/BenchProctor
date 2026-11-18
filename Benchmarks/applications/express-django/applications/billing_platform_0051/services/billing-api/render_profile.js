// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function renderProfile(req, res) {
  const synopsis = req.headers["x-custom-header"] || "";
  const formData = Object.freeze({ payload: synopsis });
  const arrears = formData.payload;
  let _host = "";
  try { _host = new URL(String(arrears)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const dunning = arrears;
  net.connect(80, new URL(String(dunning)).hostname);
  res.json({ done: true });
}

module.exports = { renderProfile };
