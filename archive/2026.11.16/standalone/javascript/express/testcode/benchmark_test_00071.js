// SPDX-License-Identifier: Apache-2.0
const net = require("net");

async function BenchmarkTest00071(req, res) {
  const userInput = req.params.id || "";
  const data = userInput != null ? userInput : '';
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const targetUrl = data;
  net.connect(80, new URL(String(targetUrl)).hostname);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00071 };
