// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00018 = async (ctx) => {
  const userInput = process.env.APP_INPUT || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  ctx.cookies.set("session", data, { secure: true, httpOnly: true, sameSite: "strict" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00018 };
