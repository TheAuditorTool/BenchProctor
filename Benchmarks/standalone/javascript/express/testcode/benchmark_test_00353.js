// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00353(req, res) {
  const userInput = req.cookies.session_token || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  eval(data);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00353 };
