// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00591 = async (ctx) => {
  const userInput = (ctx.request.files && ctx.request.files.file && ctx.request.files.file.name) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const token = String(data).slice(0, 8) + "-" + Math.floor(Math.random() * 1e12).toString(36);
  ctx.body = { token };
}

module.exports = { BenchmarkTest00591 };
