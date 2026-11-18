// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function exportProfile(req, res) {
  const phrase = req.cookies.session_token || "";
  const _input = String(phrase);
  let parcel;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': parcel = _input.normalize('NFC'); break;
    default: parcel = _input; break;
  }
  let _host = "";
  try { _host = new URL(String(parcel)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const consignment = parcel;
  net.connect(80, new URL(String(consignment)).hostname);
  res.json({ done: true });
}

module.exports = { exportProfile };
