// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00578(req, res) {
  const userInput = req.headers.origin || "";
  const data = String(userInput).slice(0, 200);
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const targetUrl = data;
  res.redirect(targetUrl);
}

module.exports = { BenchmarkTest00578 };
