// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00142 = async (ctx) => {
  const userInput = ctx.request.headers.host || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  ctx.session.data = String(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00142 };
