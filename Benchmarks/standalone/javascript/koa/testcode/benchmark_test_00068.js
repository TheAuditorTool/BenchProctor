// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00068 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const data = userInput != null ? userInput : '';
  ctx.body = "<div>" + data + "</div>";
}

module.exports = { BenchmarkTest00068 };
