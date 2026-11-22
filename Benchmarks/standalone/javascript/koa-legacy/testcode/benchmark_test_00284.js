// SPDX-License-Identifier: Apache-2.0
const vm = require("node:vm");

const BenchmarkTest00284 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  vm.runInNewContext(String(data), { Math });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00284 };
