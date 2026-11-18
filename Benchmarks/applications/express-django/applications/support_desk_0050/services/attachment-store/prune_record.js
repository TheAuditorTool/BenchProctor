// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function pruneRecord(req, res) {
  const remark = req.headers["x-custom-header"] || "";
  const formData = Object.freeze({ payload: remark });
  const inquiry = formData.payload;
  let _host = "";
  try { _host = new URL(String(inquiry)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const grievance = inquiry;
  net.connect(80, new URL(String(grievance)).hostname);
  res.json({ done: true });
}

module.exports = { pruneRecord };
