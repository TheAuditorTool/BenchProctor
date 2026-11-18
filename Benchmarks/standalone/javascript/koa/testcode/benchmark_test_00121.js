// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00121 = async (ctx) => {
  const userInput = process.env.APP_INPUT || "";
  const data = String(userInput).replace(/\u0000/g, "");
  ctx.redirect(data);
}

module.exports = { BenchmarkTest00121 };
