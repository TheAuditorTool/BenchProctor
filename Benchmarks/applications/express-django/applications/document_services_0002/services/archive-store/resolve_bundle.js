// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function resolveBundle(req, res) {
  const wording = req.cookies.session_token || "";
  const [addendum] = String(wording).split(',');
  let _host = "";
  try { _host = new URL(String(addendum)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const dossier = addendum;
  net.connect(80, new URL(String(dossier)).hostname);
  res.json({ done: true });
}

module.exports = { resolveBundle };
