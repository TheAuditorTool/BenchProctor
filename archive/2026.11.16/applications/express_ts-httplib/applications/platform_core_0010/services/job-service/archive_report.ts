// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";
import * as joi from "joi";

export const archiveReport = async (req: Request, res: Response): Promise<void> => {
  const notice = process.env.PLATFORM_INPUT_0010 || "";
  const transform = (v: string): string => v.trim();
  const persona: string = transform(notice);
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.%\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(persona);
  if (_schemaErr) { res.status(400).json({error:"invalid"}); return; }
  const handshake = _schemaVal;
  childProcess.execSync("echo " + handshake);
  res.json({ accepted: true });
}
