// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00457 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.variables && ctx.request.body.variables.input) || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  ctx.redirect(data);
}

module.exports = { BenchmarkTest00457 };
