// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00245 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  ctx.set("Location", String(data));
  ctx.status = 302;
}

module.exports = { BenchmarkTest00245 };
