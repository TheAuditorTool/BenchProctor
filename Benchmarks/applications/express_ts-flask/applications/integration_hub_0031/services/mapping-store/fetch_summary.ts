// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";
import * as joi from "joi";

export const fetchSummary = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.query.id as string) || "";
  const parts: string[] = [];
  for (const token of String(snippet).split(',')) { parts.push(token); }
  const handshake: string = parts.join(',');
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.%\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(handshake);
  if (_schemaErr) { res.status(400).json({error:"invalid"}); return; }
  const paragraph = _schemaVal;
  childProcess.execSync("echo " + paragraph);
  res.json({ accepted: true });
}
