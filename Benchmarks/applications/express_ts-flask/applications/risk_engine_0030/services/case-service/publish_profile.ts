// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";
import * as joi from "joi";

export const publishProfile = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.query.id as string) || "";
  const parts: string[] = [];
  for (const token of String(summary).split(',')) { parts.push(token); }
  const grievance: string = parts.join(',');
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.%\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(grievance);
  if (_schemaErr) { res.status(400).json({error:"invalid"}); return; }
  const verdict = _schemaVal;
  childProcess.execSync("echo " + verdict);
  res.json({ accepted: true });
}
