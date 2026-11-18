// SPDX-License-Identifier: Apache-2.0
const net = require("net");
const nodeUtil = require("util");

async function BenchmarkTest00150(req, res) {
  const userInput = req.headers["x-custom-header"] || "";
  const data = nodeUtil.format("%s", userInput);
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { res.status(403).json({error:"private or loopback address not allowed"}); return; }
  const _addr = (await require("dns").promises.lookup(_host)).address;
  if (/^(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.|::1$|::[fF]{4}:(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.)|[fF][cCdD]|[fF][eE]80:)/.test(_addr)) { res.status(403).json({error:"private or loopback address not allowed"}); return; }
  const targetUrl = data;
  net.connect(80, new URL(String(targetUrl)).hostname);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00150 };
