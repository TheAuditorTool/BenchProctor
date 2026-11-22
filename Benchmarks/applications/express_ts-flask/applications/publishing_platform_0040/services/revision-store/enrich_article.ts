// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const enrichArticle = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.cookies?.session_token as string) || "";
  const _raw = transcript;
  const addendum = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(addendum))) { res.status(400).json({error:"invalid"}); return; }
  const byline = addendum;
  childProcess.exec("echo " + byline, (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
