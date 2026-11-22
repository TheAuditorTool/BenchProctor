// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00344 = async (ctx) => {
  const userInput = (await (await fetch("https://api.partner.example/v1/records")).json()).data || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  const targetUrl = data;
  ctx.set("Location", String(targetUrl));
  ctx.status = 302;
}

module.exports = { BenchmarkTest00344 };
