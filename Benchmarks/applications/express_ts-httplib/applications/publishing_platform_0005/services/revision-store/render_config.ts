// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";
import * as joi from "joi";

export const renderConfig = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.headers.authorization as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(footnote);
  const byline: string = readInput();
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.%\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(byline);
  if (_schemaErr) { res.status(400).json({error:"invalid"}); return; }
  const addendum = _schemaVal;
  childProcess.execSync("echo " + addendum);
  res.json({ accepted: true });
}
