// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00245 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  ctx.body = "<div>" + userInput + "</div>";
}

module.exports = { BenchmarkTest00245 };
