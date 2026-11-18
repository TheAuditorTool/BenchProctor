// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

async function BenchmarkTest00072(req, res) {
  const userInput = (await (await fetch("https://api.partner.example/v1/records")).json()).data || "";
  const data = nodeUtil.format("%s", userInput);
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const targetUrl = data;
  res.redirect(targetUrl);
}

module.exports = { BenchmarkTest00072 };
