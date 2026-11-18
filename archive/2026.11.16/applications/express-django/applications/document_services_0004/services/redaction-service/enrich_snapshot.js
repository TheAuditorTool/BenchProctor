// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const joi = require("joi");

async function enrichSnapshot(req, res) {
  const excerpt = req.cookies.session_token || "";
  const dossier = excerpt != null ? excerpt : '';
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.%\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(dossier);
  if (_schemaErr) { res.status(400).json({error:"invalid"}); return; }
  const addendum = _schemaVal;
  childProcess.execSync("echo " + addendum);
  res.json({ done: true });
}

module.exports = { enrichSnapshot };
