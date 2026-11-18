// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00104 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  ctx.redirect(data);
}

module.exports = { BenchmarkTest00104 };
