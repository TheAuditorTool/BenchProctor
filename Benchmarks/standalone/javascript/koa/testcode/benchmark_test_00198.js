// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00198 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const pending = String(userInput).split(',');
  const collected = [];
  while (pending.length) { collected.push(pending.shift()); }
  const data = collected.join(',');
  ctx.set("Location", String(data));
  ctx.status = 302;
}

module.exports = { BenchmarkTest00198 };
