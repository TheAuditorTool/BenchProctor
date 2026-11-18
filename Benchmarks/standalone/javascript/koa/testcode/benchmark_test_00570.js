// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00570 = async (ctx) => {
  const userInput = ctx.request.headers.origin || "";
  const data = String(userInput).slice(0, 200);
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  const targetUrl = data;
  ctx.redirect(targetUrl);
}

module.exports = { BenchmarkTest00570 };
