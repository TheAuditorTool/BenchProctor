// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00543 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  let data;
  try { data = JSON.parse(userInput).value || ""; }
  catch (e) { data = String(userInput); }
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  const targetUrl = data;
  ctx.redirect(targetUrl);
}

module.exports = { BenchmarkTest00543 };
