// SPDX-License-Identifier: Apache-2.0

const BenchmarkTest00355 = async (ctx) => {
  const userInput = (ctx.request.body && ctx.request.body.multipart_field) || "";
  const _input = String(userInput);
  let data;
  switch (_input.startsWith('{') ? 'json' : 'text') {
    case 'json': data = _input.normalize('NFC'); break;
    default: data = _input; break;
  }
  ctx.respond = false;
  return ctx.res.writeHead(303, { Location: String(data) }).end();
}

module.exports = { BenchmarkTest00355 };
