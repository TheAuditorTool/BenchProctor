// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const formatRedaction = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.cookies?.session_token as string) || "";
  const _raw = phrase;
  const dossier = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(dossier))) { res.status(400).json({error:"invalid"}); return; }
  const addendum = dossier;
  childProcess.exec("echo " + addendum, (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
