// SPDX-License-Identifier: Apache-2.0
const { db } = require("./shared");
const http = require("http");

const BenchmarkTest00166 = async (ctx) => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const capture = (v) => () => String(v).trim();
  const readInput = capture(userInput);
  const data = readInput();
  let _host = "";
  try { _host = new URL(String(data)).hostname; } catch (e) { ctx.status = 403; ctx.body = {error:"private or loopback address not allowed"}; return; }
  const _addr = (await require("dns").promises.lookup(_host)).address;
  if (/^(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.|::1$|::[fF]{4}:(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.)|[fF][cCdD]|[fF][eE]80:)/.test(_addr)) { ctx.status = 403; ctx.body = {error:"private or loopback address not allowed"}; return; }
  const targetUrl = data;
  http.get(targetUrl);
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00166 };
