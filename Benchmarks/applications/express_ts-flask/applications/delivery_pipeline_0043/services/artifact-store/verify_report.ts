// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const verifyReport = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.cookies?.session_token as string) || "";
  const _raw = remark;
  const note = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(note))) { res.status(400).json({error:"invalid"}); return; }
  const phrase = note;
  childProcess.exec("echo " + phrase, (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
