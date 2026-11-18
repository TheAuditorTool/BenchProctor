// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00579 = async (ctx) => {
  const userInput = ctx.request.headers["user-agent"] || "";
  const data = userInput != null ? userInput : '';
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(data)) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  ctx.body = "<div>" + processed + "</div>";
}

module.exports = { BenchmarkTest00579 };
