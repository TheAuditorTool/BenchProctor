// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function BenchmarkTest00014(req, res) {
  const userInput = req.cookies.session_token || "";
  const data = String(userInput).slice(0, 200);
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { res.status(403).json({error:"private or loopback address not allowed"}); return; }
  const _addr = (await require("dns").promises.lookup(_host)).address;
  if (/^(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.|::1$|::[fF]{4}:(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.)|[fF][cCdD]|[fF][eE]80:)/.test(_addr)) { res.status(403).json({error:"private or loopback address not allowed"}); return; }
  const targetUrl = data;
  http.get(targetUrl);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00014 };
