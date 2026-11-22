// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00358 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.variables && ctx.request.body.variables.input) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  ctx.app.context.announcement = String(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00358 };
