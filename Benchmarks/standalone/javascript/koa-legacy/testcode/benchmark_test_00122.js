// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00122 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  if (!/^(asc|desc|name|created)$/.test(String(data))) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  new Function("return (" + String(processed) + ");")();
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00122 };
