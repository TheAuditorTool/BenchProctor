// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

const BenchmarkTest00102 = async (ctx) => {
  const userInput = (ctx.request.files && ctx.request.files.file && ctx.request.files.file.name) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  nodeSerialize.unserialize(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00102 };
