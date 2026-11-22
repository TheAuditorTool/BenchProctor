// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00301 = async (ctx) => {
  const userInput = ctx.params.id || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  ctx.set("Location", String(data));
  ctx.status = 302;
}

module.exports = { BenchmarkTest00301 };
