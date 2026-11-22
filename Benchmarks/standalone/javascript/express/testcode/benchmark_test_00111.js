// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00111(req, res) {
  const userInput = req.params.id || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const targetUrl = data;
  res.location(String(targetUrl)).sendStatus(303); return;
}

module.exports = { BenchmarkTest00111 };
