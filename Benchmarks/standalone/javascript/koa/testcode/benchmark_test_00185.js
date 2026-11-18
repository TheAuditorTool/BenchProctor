// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00185 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(data)) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  ctx.body = "<div>" + processed + "</div>";
}

module.exports = { BenchmarkTest00185 };
