// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00208(req, res) {
  const userInput = req.query.id || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  const planQuotas = new Map([["basic", { quota: 10 }], ["team", { quota: 50 }], ["enterprise", { quota: 500 }]]);
  const { quota } = planQuotas.get(String(data));
  res.json({ quota }); return;
}

module.exports = { BenchmarkTest00208 };
