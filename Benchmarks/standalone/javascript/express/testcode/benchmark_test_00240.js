// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00240(req, res) {
  const userInput = (req.files && req.files[0] && req.files[0].originalname) || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const targetUrl = data;
  return res.status(302).set("Location", String(targetUrl)).end();
}

module.exports = { BenchmarkTest00240 };
