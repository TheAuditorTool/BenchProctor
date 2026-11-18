// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00030(req, res) {
  const userInput = req.body || "";
  let _host = "";
  try { _host = new URL(String(userInput)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const targetUrl = userInput;
  res.redirect(targetUrl);
}

module.exports = { BenchmarkTest00030 };
