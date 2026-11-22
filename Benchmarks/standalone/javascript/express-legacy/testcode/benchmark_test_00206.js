// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00206(req, res) {
  const userInput = (req.files && req.files[0] && req.files[0].originalname) || "";
  const planQuotas = new Map([["basic", { quota: 10 }], ["team", { quota: 50 }], ["enterprise", { quota: 500 }]]);
  const { quota } = planQuotas.get(String(userInput));
  res.json({ quota }); return;
}

module.exports = { BenchmarkTest00206 };
