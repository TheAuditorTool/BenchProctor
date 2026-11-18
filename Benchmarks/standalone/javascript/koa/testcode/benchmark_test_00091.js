// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00091 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  ctx.body = "<div>" + data + "</div>";
}

module.exports = { BenchmarkTest00091 };
