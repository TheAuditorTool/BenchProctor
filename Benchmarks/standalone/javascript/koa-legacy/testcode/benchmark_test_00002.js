// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00002 = async (ctx) => {
  const userInput = ctx.request.headers.origin || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  const planQuotas = new Map([["basic", { quota: 10 }], ["team", { quota: 50 }], ["enterprise", { quota: 500 }]]);
  const plan = planQuotas.get(String(data));
  if (!plan) { ctx.status = 404; ctx.body = { error: "unknown plan" }; return; }
  const { quota } = plan;
  ctx.body = { quota }; return;
}

module.exports = { BenchmarkTest00002 };
