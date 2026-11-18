// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00063 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { ctx.status = 403; ctx.body = {error:"host not allowed"}; return; }
  const targetUrl = data;
  ctx.redirect(targetUrl);
}

module.exports = { BenchmarkTest00063 };
