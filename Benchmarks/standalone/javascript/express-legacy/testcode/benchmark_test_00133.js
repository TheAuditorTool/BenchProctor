// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00133(req, res) {
  const userInput = (req.files && req.files[0] && req.files[0].originalname) || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  const planQuotas = new Map([["basic", { quota: 10 }], ["team", { quota: 50 }], ["enterprise", { quota: 500 }]]);
  const { quota } = planQuotas.get(String(data));
  res.json({ quota }); return;
}

module.exports = { BenchmarkTest00133 };
