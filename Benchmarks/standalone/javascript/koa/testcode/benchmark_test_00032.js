// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00032 = async (ctx) => {
  const userInput = ctx.request.rawBody || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  const domain = String(data).match(/@([A-Za-z0-9.-]+)$/)[1];
  ctx.body = { domain }; return;
}

module.exports = { BenchmarkTest00032 };
