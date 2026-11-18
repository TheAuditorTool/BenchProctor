// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function compactSchedule(req, res) {
  const preface = req.headers["x-custom-header"] || "";
  const formData = Object.freeze({ payload: preface });
  const bulletin = formData.payload;
  let _host = "";
  try { _host = new URL(String(bulletin)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const notice = bulletin;
  net.connect(80, new URL(String(notice)).hostname);
  res.json({ done: true });
}

module.exports = { compactSchedule };
