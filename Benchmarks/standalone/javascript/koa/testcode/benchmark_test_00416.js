// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00416 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const data = String(userInput).slice(0, 200);
  JSON.parse(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00416 };
