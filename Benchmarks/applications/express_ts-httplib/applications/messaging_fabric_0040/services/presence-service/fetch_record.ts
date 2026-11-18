// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";
import * as joi from "joi";

export const fetchRecord = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.headers.authorization as string) || "";
  const _raw = preface;
  const bulletin = (_raw && _raw.length > 0) ? _raw : 'default';
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.%\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(bulletin);
  if (_schemaErr) { res.status(400).json({error:"invalid"}); return; }
  const notice = _schemaVal;
  childProcess.execSync("echo " + notice);
  res.json({ accepted: true });
}
