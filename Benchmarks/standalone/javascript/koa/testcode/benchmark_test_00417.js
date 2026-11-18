// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00417 = async (ctx) => {
  const userInput = ctx.request.headers["user-agent"] || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  ctx.body = "<div>" + data + "</div>";
}

module.exports = { BenchmarkTest00417 };
