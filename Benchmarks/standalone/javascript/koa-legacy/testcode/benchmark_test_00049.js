// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00049 = async (ctx) => {
  const userInput = (ctx.request.files && ctx.request.files.file && ctx.request.files.file.name) || "";
  const planQuotas = new Map([["basic", { quota: 10 }], ["team", { quota: 50 }], ["enterprise", { quota: 500 }]]);
  const { quota } = planQuotas.get(String(userInput));
  ctx.body = { quota }; return;
}

module.exports = { BenchmarkTest00049 };
