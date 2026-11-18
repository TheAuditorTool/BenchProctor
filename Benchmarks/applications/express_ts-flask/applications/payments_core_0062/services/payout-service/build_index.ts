// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";
import * as joi from "joi";

export const buildIndex = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.query.id as string) || "";
  const parts: string[] = [];
  for (const token of String(headline).split(',')) { parts.push(token); }
  const disbursement: string = parts.join(',');
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.%\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(disbursement);
  if (_schemaErr) { res.status(400).json({error:"invalid"}); return; }
  const remittance = _schemaVal;
  childProcess.execSync("echo " + remittance);
  res.json({ accepted: true });
}
