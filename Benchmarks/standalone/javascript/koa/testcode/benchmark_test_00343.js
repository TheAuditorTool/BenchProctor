// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00343 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  ctx.body = "<div>" + data + "</div>";
}

module.exports = { BenchmarkTest00343 };
