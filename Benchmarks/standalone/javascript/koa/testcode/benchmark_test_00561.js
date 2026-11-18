// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00561 = async (ctx) => {
  const userInput = ctx.request.headers.origin || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  ctx.redirect(data);
}

module.exports = { BenchmarkTest00561 };
