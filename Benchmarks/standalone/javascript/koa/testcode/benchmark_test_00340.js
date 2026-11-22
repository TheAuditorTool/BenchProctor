// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00340 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  function normalize(value) { return String(value).normalize("NFC"); }
  const data = normalize(userInput);
  const token = String(data).slice(0, 8) + "-" + Math.floor(Math.random() * 1e12).toString(36);
  ctx.body = { token };
}

module.exports = { BenchmarkTest00340 };
