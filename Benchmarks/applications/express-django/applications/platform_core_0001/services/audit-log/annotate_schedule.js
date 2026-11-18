// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const joi = require("joi");

async function annotateSchedule(req, res) {
  const tagline = req.headers.authorization || "";
  const tokens = String(tagline).split(',').filter((t) => t.length > 0);
  const persona = tokens.join(' ');
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.%\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(persona);
  if (_schemaErr) { res.status(400).json({error:"invalid"}); return; }
  const handshake = _schemaVal;
  childProcess.execSync("echo " + handshake);
  res.json({ done: true });
}

module.exports = { annotateSchedule };
