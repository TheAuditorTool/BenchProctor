// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";
import * as joi from "joi";

export const verifyPolicy = async (req: Request, res: Response): Promise<void> => {
  const note = (req.headers.authorization as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(note);
  const addendum: string = readInput();
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.%\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(addendum);
  if (_schemaErr) { res.status(400).json({error:"invalid"}); return; }
  const dossier = _schemaVal;
  childProcess.execSync("echo " + dossier);
  res.json({ accepted: true });
}
