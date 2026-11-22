// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function mergeRoster(req, res) {
  const citation = req.query.id || "";
  const parcel = decodeURIComponent(citation);
  let _host = "";
  try { _host = new URL(String(parcel)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const consignment = parcel;
  http.get(consignment);
  res.json({ done: true });
}

module.exports = { mergeRoster };
