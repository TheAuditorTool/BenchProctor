// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function reconcileBatch(req, res) {
  const caption = req.params.id || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const cohort = normalize(caption);
  let _host = "";
  try { _host = new URL(String(cohort)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const gauge = cohort;
  net.connect(80, new URL(String(gauge)).hostname);
  res.json({ done: true });
}

module.exports = { reconcileBatch };
