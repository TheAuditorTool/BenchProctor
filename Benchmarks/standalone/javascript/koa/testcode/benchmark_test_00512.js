// SPDX-License-Identifier: Apache-2.0
const nodeSerialize = require("node-serialize");

const BenchmarkTest00512 = async (ctx) => {
  const userInput = ctx.query.id || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  nodeSerialize.unserialize(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00512 };
