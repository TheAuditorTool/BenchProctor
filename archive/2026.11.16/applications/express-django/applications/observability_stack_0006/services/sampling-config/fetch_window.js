// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function fetchWindow(req, res) {
  const preface = req.body.payload || "";
  const cohort = preface != null ? preface : '';
  let _host = "";
  try { _host = new URL(String(cohort)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const gauge = cohort;
  net.connect(80, new URL(String(gauge)).hostname);
  res.json({ done: true });
}

module.exports = { fetchWindow };
