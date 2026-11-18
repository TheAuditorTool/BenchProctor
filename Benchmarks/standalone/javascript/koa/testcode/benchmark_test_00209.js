// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00209 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  const [data] = String(userInput).split(',');
  ctx.body = "<div>" + data + "</div>";
}

module.exports = { BenchmarkTest00209 };
