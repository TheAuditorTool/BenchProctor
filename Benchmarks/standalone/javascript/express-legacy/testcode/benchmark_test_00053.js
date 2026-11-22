// SPDX-License-Identifier: Apache-2.0
const http = require("http");

async function BenchmarkTest00053(req, res) {
  const userInput = req.cookies.session_token || "";
  const data = `${userInput}`;
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const targetUrl = data;
  http.get(targetUrl);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00053 };
