// SPDX-License-Identifier: Apache-2.0
const net = require("net");
const nodeUtil = require("util");

async function BenchmarkTest00316(req, res) {
  const userInput = (req.file && req.file.originalname) || "";
  const data = nodeUtil.format("%s", userInput);
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const targetUrl = data;
  net.connect(80, new URL(String(targetUrl)).hostname);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00316 };
