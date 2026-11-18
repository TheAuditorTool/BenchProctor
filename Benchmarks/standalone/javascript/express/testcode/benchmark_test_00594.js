// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00594(req, res) {
  const userInput = req.cookies.session_token || "";
  const data = String(userInput).replace(/\u0000/g, "");
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const targetUrl = data;
  res.redirect(targetUrl);
}

module.exports = { BenchmarkTest00594 };
