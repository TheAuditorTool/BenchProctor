// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00267(req, res) {
  const userInput = req.body.field || "";
  const parts = [];
  for (const token of String(userInput).split(',')) { parts.push(token); }
  const data = parts.join(',');
  const planQuotas = new Map([["basic", { quota: 10 }], ["team", { quota: 50 }], ["enterprise", { quota: 500 }]]);
  const { quota } = planQuotas.get(String(data));
  res.json({ quota }); return;
}

module.exports = { BenchmarkTest00267 };
