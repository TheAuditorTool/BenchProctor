// SPDX-License-Identifier: Apache-2.0

async function BenchmarkTest00108(req, res) {
  const userInput = req.body.multipart_field || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  res.location(String(data)).sendStatus(303); return;
}

module.exports = { BenchmarkTest00108 };
