// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

const BenchmarkTest00434 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  ctx.body = escapeHtml(userInput);
}

module.exports = { BenchmarkTest00434 };
