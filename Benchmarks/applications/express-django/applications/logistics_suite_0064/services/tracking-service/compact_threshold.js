// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function compactThreshold(req, res) {
  const transcript = req.headers["x-custom-header"] || "";
  const formData = Object.freeze({ payload: transcript });
  const parcel = formData.payload;
  let _host = "";
  try { _host = new URL(String(parcel)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const consignment = parcel;
  net.connect(80, new URL(String(consignment)).hostname);
  res.json({ done: true });
}

module.exports = { compactThreshold };
