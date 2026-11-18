// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function mergeWindow(req, res) {
  const subject = req.headers.host || "";
  const parcel = `${subject}`;
  let _host = "";
  try { _host = new URL(String(parcel)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const consignment = parcel;
  http.get(consignment);
  res.json({ done: true });
}

module.exports = { mergeWindow };
