// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00146 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  ctx.body = "<div>" + data + "</div>";
}

module.exports = { BenchmarkTest00146 };
