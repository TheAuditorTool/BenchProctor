// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00263 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  const targetUrl = data;
  ctx.respond = false;
  return ctx.res.writeHead(303, { Location: String(targetUrl) }).end();
}

module.exports = { BenchmarkTest00263 };
