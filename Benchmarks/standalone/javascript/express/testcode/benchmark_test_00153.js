// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00153(req, res) {
  const userInput = req.query.id || "";
  const data = `${userInput}`;
  const planQuotas = new Map([["basic", { quota: 10 }], ["team", { quota: 50 }], ["enterprise", { quota: 500 }]]);
  const plan = planQuotas.get(String(data));
  if (!plan) { res.status(404).json({ error: "unknown plan" }); return; }
  const { quota } = plan;
  res.json({ quota }); return;
}

module.exports = { BenchmarkTest00153 };
