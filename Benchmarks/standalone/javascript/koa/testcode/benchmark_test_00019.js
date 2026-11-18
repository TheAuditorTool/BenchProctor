// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00019 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  ctx.body = "<div>" + data + "</div>";
}

module.exports = { BenchmarkTest00019 };
