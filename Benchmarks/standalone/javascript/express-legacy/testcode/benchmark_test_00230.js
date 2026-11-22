// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function BenchmarkTest00230(req, res) {
  const userInput = req.headers.referer || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const targetUrl = data;
  http.get(targetUrl);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00230 };
