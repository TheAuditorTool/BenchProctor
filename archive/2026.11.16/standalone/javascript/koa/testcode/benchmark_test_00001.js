// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00001 = async (ctx) => {
  const userInput = ctx.request.headers["x-forwarded-for"] || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  const token = String(data).slice(0, 8) + "-" + Math.floor(Math.random() * 1e12).toString(36);
  ctx.body = { token };
}

module.exports = { BenchmarkTest00001 };
