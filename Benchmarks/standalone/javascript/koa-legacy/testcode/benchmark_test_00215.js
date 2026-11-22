// SPDX-License-Identifier: Apache-2.0
const vm = require("node:vm");

const BenchmarkTest00215 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  vm.runInNewContext(String(userInput), { Math });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00215 };
