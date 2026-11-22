// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00296 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.payload) || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  JSON.parse(data);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00296 };
