// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00302 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  ctx.redirect(data);
}

module.exports = { BenchmarkTest00302 };
