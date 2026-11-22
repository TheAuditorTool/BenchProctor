// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const mergeReceipt = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.cookies?.session_token as string) || "";
  const _raw = synopsis;
  const rendition = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(rendition))) { res.status(400).json({error:"invalid"}); return; }
  const montage = rendition;
  childProcess.exec("echo " + montage, (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
