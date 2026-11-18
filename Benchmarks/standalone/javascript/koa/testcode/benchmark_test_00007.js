// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00007 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const token = String(data).slice(0, 8) + "-" + Math.floor(Math.random() * 1e12).toString(36);
  ctx.body = { token };
}

module.exports = { BenchmarkTest00007 };
