// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function reconcileProfile(req, res) {
  const passage = req.params.id || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const montage = normalize(passage);
  let _host = "";
  try { _host = new URL(String(montage)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const rendition = montage;
  net.connect(80, new URL(String(rendition)).hostname);
  res.json({ done: true });
}

module.exports = { reconcileProfile };
