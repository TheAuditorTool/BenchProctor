// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00528 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.variables && ctx.request.body.variables.input) || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  ctx.redirect(data);
}

module.exports = { BenchmarkTest00528 };
