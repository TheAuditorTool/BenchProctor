// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00212(req, res) {
  const userInput = (req.files && req.files[0] && req.files[0].originalname) || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  const planQuotas = new Map([["basic", { quota: 10 }], ["team", { quota: 50 }], ["enterprise", { quota: 500 }]]);
  const { quota } = planQuotas.get(String(data));
  res.json({ quota }); return;
}

module.exports = { BenchmarkTest00212 };
