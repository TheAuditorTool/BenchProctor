// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00001 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  ctx.body = "<div>" + data + "</div>";
}

module.exports = { BenchmarkTest00001 };
