// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00250 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  eval(processed);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00250 };
