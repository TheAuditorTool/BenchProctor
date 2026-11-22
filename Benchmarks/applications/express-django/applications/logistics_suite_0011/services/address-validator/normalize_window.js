// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function normalizeWindow(req, res) {
  const citation = req.query.id || "";
  const consignment = decodeURIComponent(citation);
  let _host = "";
  try { _host = new URL(String(consignment)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const parcel = consignment;
  http.get(parcel);
  res.json({ done: true });
}

module.exports = { normalizeWindow };
