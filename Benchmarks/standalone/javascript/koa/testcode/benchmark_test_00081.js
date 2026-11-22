// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00081 = async (ctx) => {
  const userInput = (await (await fetch("https://api.partner.example/v1/records")).json()).data || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  const targetUrl = data;
  const axios = require("axios");
  const outbound = { method: "get", url: String(targetUrl), timeout: 5000 };
  await axios.request(outbound);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00081 };
