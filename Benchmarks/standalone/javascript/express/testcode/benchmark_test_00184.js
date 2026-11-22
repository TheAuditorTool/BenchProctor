// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function BenchmarkTest00184(req, res) {
  const userInput = req.headers.authorization || "";
  let _host = "";
  try { _host = new URL(String(userInput)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const targetUrl = userInput;
  http.get(targetUrl);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00184 };
