// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00144 = async (ctx) => {
  const userInput = (ctx.request.files && ctx.request.files.file && ctx.request.files.file.name) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  eval(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00144 };
