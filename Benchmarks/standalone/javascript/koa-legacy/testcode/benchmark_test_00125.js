// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00125 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(data)) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  ctx.body = "<div>" + processed + "</div>";
}

module.exports = { BenchmarkTest00125 };
