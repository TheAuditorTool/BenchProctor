// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00183 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const [data] = String(userInput).split(',');
  ctx.body = "<div>" + data + "</div>";
}

module.exports = { BenchmarkTest00183 };
