// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00043 = async (ctx) => {
  const userInput = ctx.request.headers.referer || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  JSON.parse(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00043 };
