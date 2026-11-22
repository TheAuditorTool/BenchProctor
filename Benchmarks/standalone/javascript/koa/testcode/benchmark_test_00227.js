// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00227 = async (ctx) => {
  const userInput = ctx.cookies.get("session_token") || "";
  const data = userInput != null ? userInput : '';
  const planQuotas = new Map([["basic", { quota: 10 }], ["team", { quota: 50 }], ["enterprise", { quota: 500 }]]);
  const plan = planQuotas.get(String(data));
  if (!plan) { ctx.status = 404; ctx.body = { error: "unknown plan" }; return; }
  const { quota } = plan;
  ctx.body = { quota }; return;
}

module.exports = { BenchmarkTest00227 };
