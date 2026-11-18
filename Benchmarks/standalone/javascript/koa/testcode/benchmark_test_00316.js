// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00316 = async (ctx) => {
  const userInput = process.env.APP_INPUT || "";
  const data = `${userInput}`;
  ctx.redirect(data);
}

module.exports = { BenchmarkTest00316 };
