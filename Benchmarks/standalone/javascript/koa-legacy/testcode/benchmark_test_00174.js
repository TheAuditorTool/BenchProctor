// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00174 = async (ctx) => {
  const userInput = ctx.request.headers.origin || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  if (!/^(asc|desc|name|created)$/.test(String(data))) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = data;
  eval(processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00174 };
