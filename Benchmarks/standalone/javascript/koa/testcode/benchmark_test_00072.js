// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00072 = async (ctx) => {
  const userInput = ctx.params.id || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const token = String(data).slice(0, 8) + "-" + Math.floor(Math.random() * 1e12).toString(36);
  ctx.body = { token };
}

module.exports = { BenchmarkTest00072 };
