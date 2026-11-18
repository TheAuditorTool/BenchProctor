// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00504(req, res) {
  const userInput = req.params.id || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  req.session.data = String(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00504 };
