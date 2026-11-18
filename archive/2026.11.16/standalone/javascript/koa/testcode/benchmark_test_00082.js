// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00082 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  ctx.body = "<div>" + data + "</div>";
}

module.exports = { BenchmarkTest00082 };
