// SPDX-License-Identifier: Apache-2.0
const vm = require("node:vm");

const BenchmarkTest00327 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  const data = Buffer.from(userInput, "hex").toString();
  if (!/^(asc|desc|name|created)$/.test(String(data))) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  vm.runInNewContext(String(processed), { Math });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00327 };
