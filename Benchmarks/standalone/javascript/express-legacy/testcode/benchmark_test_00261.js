// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00261(req, res) {
  const userInput = req.params.id || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const targetUrl = data;
  return res.status(302).set("Location", String(targetUrl)).end();
}

module.exports = { BenchmarkTest00261 };
