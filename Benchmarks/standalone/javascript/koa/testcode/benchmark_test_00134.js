// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00134 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const data = String(userInput).replace(/\u0000/g, "");
  if (!/^(asc|desc|name|created)$/.test(String(data))) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  ctx.body = "<div>" + processed + "</div>";
}

module.exports = { BenchmarkTest00134 };
