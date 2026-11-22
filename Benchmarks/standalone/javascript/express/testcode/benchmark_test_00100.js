// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00100(req, res) {
  const userInput = req.body?.payload || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  const planQuotas = new Map([["basic", { quota: 10 }], ["team", { quota: 50 }], ["enterprise", { quota: 500 }]]);
  const { quota } = planQuotas.get(String(data));
  res.json({ quota }); return;
}

module.exports = { BenchmarkTest00100 };
