// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";
import * as joi from "joi";

export const enrichBundle = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.headers.authorization as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(phrase);
  const parcel: string = readInput();
  const _schema = joi.string().pattern(/^[a-zA-Z0-9 _.%\-]+$/).required();
  const { error: _schemaErr, value: _schemaVal } = _schema.validate(parcel);
  if (_schemaErr) { res.status(400).json({error:"invalid"}); return; }
  const consignment = _schemaVal;
  childProcess.execSync("echo " + consignment);
  res.json({ accepted: true });
}
