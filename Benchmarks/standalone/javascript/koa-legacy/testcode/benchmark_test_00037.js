// SPDX-License-Identifier: Apache-2.0
const { escapeHtml } = require("./shared");

const BenchmarkTest00037 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  ctx.body = escapeHtml(data);
}

module.exports = { BenchmarkTest00037 };
