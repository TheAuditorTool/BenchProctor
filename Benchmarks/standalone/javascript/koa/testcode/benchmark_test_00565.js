// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00565 = async (ctx) => {
  const userInput = ctx.request.headers["user-agent"] || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  ctx.body = "<div>" + data + "</div>";
}

module.exports = { BenchmarkTest00565 };
