// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00053(req, res) {
  const userInput = (await (await fetch("https://api.partner.example/v1/records")).json()).data || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const targetUrl = data;
  const axios = require("axios");
  const outbound = { method: "get", url: String(targetUrl), timeout: 5000 };
  await axios.request(outbound);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00053 };
