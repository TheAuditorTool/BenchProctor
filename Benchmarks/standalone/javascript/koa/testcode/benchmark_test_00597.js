// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00597 = async (ctx) => {
  const userInput = ctx.request.headers.authorization || "";
  const data = Buffer.from(userInput, "hex").toString();
  ctx.redirect(data);
}

module.exports = { BenchmarkTest00597 };
