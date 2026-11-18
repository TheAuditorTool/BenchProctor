// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00433 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const trim = (v) => String(v).trim();
  const data = trim(userInput);
  ctx.body = "<div>" + data + "</div>";
}

module.exports = { BenchmarkTest00433 };
