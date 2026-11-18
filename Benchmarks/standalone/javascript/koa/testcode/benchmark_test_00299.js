// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00299 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  JSON.parse(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00299 };
