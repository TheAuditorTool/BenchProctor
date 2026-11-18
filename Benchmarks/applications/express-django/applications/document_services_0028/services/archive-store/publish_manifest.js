// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function publishManifest(req, res) {
  const note = req.cookies.session_token || "";
  const _input = String(note);
  let addendum;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': addendum = _input.normalize('NFC'); break;
    default: addendum = _input; break;
  }
  let _host = "";
  try { _host = new URL(String(addendum)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const dossier = addendum;
  net.connect(80, new URL(String(dossier)).hostname);
  res.json({ done: true });
}

module.exports = { publishManifest };
