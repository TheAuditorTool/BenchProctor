// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00098 = async (ctx) => {
  const userInput = (ctx.request.files && ctx.request.files.file && ctx.request.files.file.name) || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  const planQuotas = new Map([["basic", { quota: 10 }], ["team", { quota: 50 }], ["enterprise", { quota: 500 }]]);
  const { quota } = planQuotas.get(String(data));
  ctx.body = { quota }; return;
}

module.exports = { BenchmarkTest00098 };
