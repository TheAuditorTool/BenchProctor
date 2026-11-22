// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function exportSchedule(req, res) {
  const wording = req.cookies.session_token || "";
  const [backorder] = String(wording).split(',');
  let _host = "";
  try { _host = new URL(String(backorder)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const voucher = backorder;
  net.connect(80, new URL(String(voucher)).hostname);
  res.json({ done: true });
}

module.exports = { exportSchedule };
