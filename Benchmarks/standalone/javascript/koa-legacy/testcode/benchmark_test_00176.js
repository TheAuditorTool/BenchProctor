// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00176 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.field) || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  const planQuotas = new Map([["basic", { quota: 10 }], ["team", { quota: 50 }], ["enterprise", { quota: 500 }]]);
  const { quota } = planQuotas.get(String(data));
  ctx.body = { quota }; return;
}

module.exports = { BenchmarkTest00176 };
