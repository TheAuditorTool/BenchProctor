// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00168(req, res) {
  const userInput = req.headers.referer || "";
  const data = `${userInput}`;
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const targetUrl = data;
  res.location(String(targetUrl)).sendStatus(303); return;
}

module.exports = { BenchmarkTest00168 };
