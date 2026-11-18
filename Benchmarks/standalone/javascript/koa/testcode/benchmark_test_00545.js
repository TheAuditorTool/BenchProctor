// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00545 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  ctx.body = "<div>" + userInput + "</div>";
}

module.exports = { BenchmarkTest00545 };
