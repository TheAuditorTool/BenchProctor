// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00306 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  const targetUrl = data;
  ctx.respond = false;
  return ctx.res.writeHead(303, { Location: String(targetUrl) }).end();
}

module.exports = { BenchmarkTest00306 };
