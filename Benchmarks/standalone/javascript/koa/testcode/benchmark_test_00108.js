// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00108 = async (ctx) => {
  const userInput = (ctx.request.files && ctx.request.files.file && ctx.request.files.file.name) || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  ctx.session.data = String(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00108 };
