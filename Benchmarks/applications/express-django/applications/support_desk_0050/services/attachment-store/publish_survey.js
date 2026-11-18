// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function publishSurvey(req, res) {
  const remark = req.params.id || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const inquiry = normalize(remark);
  let _host = "";
  try { _host = new URL(String(inquiry)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const grievance = inquiry;
  net.connect(80, new URL(String(grievance)).hostname);
  res.json({ done: true });
}

module.exports = { publishSurvey };
