// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00677(req, res) {
  const userInput = req.headers.host || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  if (!/^(asc|desc|name|created)$/.test(String(data))) { res.status(400).json({error:"invalid"}); return; }
  const processed = data;
  req.session.data = String(processed);
  res.json({ done: true });
}

module.exports = { BenchmarkTest00677 };
