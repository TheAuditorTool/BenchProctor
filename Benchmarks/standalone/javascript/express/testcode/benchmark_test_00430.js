// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00430(req, res) {
  const userInput = req.query.id || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  JSON.parse(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00430 };
