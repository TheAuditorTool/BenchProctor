// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00118 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  new Function("return (" + String(data) + ");")();
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00118 };
