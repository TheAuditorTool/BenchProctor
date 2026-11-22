// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00112 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const [data] = String(userInput).split(',');
  ctx.redirect(data);
}

module.exports = { BenchmarkTest00112 };
