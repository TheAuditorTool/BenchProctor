// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00133 = async (ctx) => {
  const userInput = (ctx.request.files && ctx.request.files.file && ctx.request.files.file.name) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  if (!/^(asc|desc|name|created)$/.test(String(data))) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  eval(processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00133 };
