// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00082 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  ctx.cookies.set("session", data, { secure: false, httpOnly: true, sameSite: "strict" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00082 };
