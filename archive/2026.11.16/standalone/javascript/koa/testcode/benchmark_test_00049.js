// SPDX-License-Identifier: Apache-2.0
const nodeUtil = require("util");

const BenchmarkTest00049 = async (ctx) => {
  const userInput = (await (await fetch("https://api.partner.example/v1/records")).json()).data || "";
  const data = nodeUtil.format("%s", userInput);
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  const targetUrl = data;
  ctx.redirect(targetUrl);
}

module.exports = { BenchmarkTest00049 };
