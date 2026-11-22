// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const joi = require("joi");

const BenchmarkTest00300 = async (ctx) => {
  const userInput = process.env.APP_INPUT || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.%\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(data);
  if (_schemaErr) { ctx.status = 400; ctx.body = {error:"invalid"}; return; }
  const processed = _schemaVal;
  childProcess.spawn("echo " + processed, { shell: true, stdio: "inherit" });
  ctx.body = { ack: true };
}

module.exports = { BenchmarkTest00300 };
