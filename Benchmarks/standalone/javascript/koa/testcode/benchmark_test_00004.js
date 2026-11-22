// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00004 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const data = `${userInput}`;
  const planQuotas = new Map([["basic", { quota: 10 }], ["team", { quota: 50 }], ["enterprise", { quota: 500 }]]);
  const plan = planQuotas.get(String(data));
  if (!plan) { ctx.status = 404; ctx.body = { error: "unknown plan" }; return; }
  const { quota } = plan;
  ctx.body = { quota }; return;
}

module.exports = { BenchmarkTest00004 };
