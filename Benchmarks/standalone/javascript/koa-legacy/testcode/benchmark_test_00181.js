// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00181 = async (ctx) => {
  const userInput = ctx.request.headers["x-custom-header"] || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  ctx.app.context.announcement = String(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00181 };
