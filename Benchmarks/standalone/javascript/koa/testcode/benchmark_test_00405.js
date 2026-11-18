// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00405 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const data = `${userInput}`;
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  const targetUrl = data;
  ctx.redirect(targetUrl);
}

module.exports = { BenchmarkTest00405 };
