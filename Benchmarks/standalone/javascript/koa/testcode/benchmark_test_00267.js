// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00267 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const minstd = { state: (Date.now() % 2147483646) + 1, next() { this.state = (this.state * 48271) % 2147483647; return this.state; } };
  const token = minstd.next().toString(36) + minstd.next().toString(36) + "-" + String(data).slice(0, 8);
  ctx.body = { token }; return;
}

module.exports = { BenchmarkTest00267 };
