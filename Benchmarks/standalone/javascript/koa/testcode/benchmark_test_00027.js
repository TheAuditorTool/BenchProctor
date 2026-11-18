// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00027 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const data = String(userInput).replace(/\u0000/g, "");
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  const targetUrl = data;
  ctx.redirect(targetUrl);
}

module.exports = { BenchmarkTest00027 };
