// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00270 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  ctx.set("Location", String(data));
  ctx.status = 302;
}

module.exports = { BenchmarkTest00270 };
