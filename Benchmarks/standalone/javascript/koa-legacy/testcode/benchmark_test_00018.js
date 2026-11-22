// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00018 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  const token = String(data).slice(0, 8) + "-" + Math.floor(Math.random() * 1e12).toString(36);
  ctx.body = { token };
}

module.exports = { BenchmarkTest00018 };
