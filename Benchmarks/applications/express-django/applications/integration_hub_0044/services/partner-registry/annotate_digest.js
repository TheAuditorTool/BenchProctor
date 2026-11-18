// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function annotateDigest(req, res) {
  const blurb = req.params.id || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const handshake = normalize(blurb);
  let _host = "";
  try { _host = new URL(String(handshake)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const citation = handshake;
  net.connect(80, new URL(String(citation)).hostname);
  res.json({ done: true });
}

module.exports = { annotateDigest };
