// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00504 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const data = userInput != null ? userInput : '';
  ctx.body = "<div>" + data + "</div>";
}

module.exports = { BenchmarkTest00504 };
