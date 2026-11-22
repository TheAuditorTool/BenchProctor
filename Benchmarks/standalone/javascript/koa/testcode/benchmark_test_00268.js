// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00268 = async (ctx) => {
  const userInput = ctx.query.id || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  const planQuotas = new Map([["basic", { quota: 10 }], ["team", { quota: 50 }], ["enterprise", { quota: 500 }]]);
  const { quota } = planQuotas.get(String(data));
  ctx.body = { quota }; return;
}

module.exports = { BenchmarkTest00268 };
