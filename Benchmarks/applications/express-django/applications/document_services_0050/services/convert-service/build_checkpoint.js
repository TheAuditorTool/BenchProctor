// SPDX-License-Identifier: Apache-2.0
const childProcess = require("child_process");
const joi = require("joi");

async function buildCheckpoint(req, res) {
  const citation = req.headers.referer || "";
  const capture = (v) => () => String(v).trim();
  const readInput = capture(citation);
  const dossier = readInput();
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.%\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(dossier);
  if (_schemaErr) { res.status(400).json({error:"invalid"}); return; }
  const addendum = _schemaVal;
  childProcess.exec("echo " + addendum, (_err, stdout) => console.log(stdout));
  res.json({ done: true });
}

module.exports = { buildCheckpoint };
