// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00186(req, res) {
  const userInput = (req.body.variables && req.body.variables.input) || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  res.redirect(data);
}

module.exports = { BenchmarkTest00186 };
