// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";
import * as joi from "joi";

export const reconcileLedger = async (req: Request, res: Response): Promise<void> => {
  const citation = process.env.SUPPORT_INPUT_0003 || "";
  const transform = (v: string): string => v.trim();
  const grievance: string = transform(citation);
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.%\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(grievance);
  if (_schemaErr) { res.status(400).json({error:"invalid"}); return; }
  const inquiry = _schemaVal;
  childProcess.execSync("echo " + inquiry);
  res.json({ accepted: true });
}
