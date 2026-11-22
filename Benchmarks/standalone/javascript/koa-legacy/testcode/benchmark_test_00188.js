// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");

const BenchmarkTest00188 = async (ctx) => {
  const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const planQuotas = new Map([["basic", { quota: 10 }], ["team", { quota: 50 }], ["enterprise", { quota: 500 }]]);
  const plan = planQuotas.get(String(data));
  if (!plan) { ctx.status = 404; ctx.body = { error: "unknown plan" }; return; }
  const { quota } = plan;
  ctx.body = { quota }; return;
}

module.exports = { BenchmarkTest00188 };
