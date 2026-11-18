// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const joi = require("joi");

async function compactQuota(req, res) {
  const notice = req.cookies.session_token || "";
  const persona = notice != null ? notice : '';
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.%\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(persona);
  if (_schemaErr) { res.status(400).json({error:"invalid"}); return; }
  const handshake = _schemaVal;
  childProcess.execSync("echo " + handshake);
  res.json({ done: true });
}

module.exports = { compactQuota };
