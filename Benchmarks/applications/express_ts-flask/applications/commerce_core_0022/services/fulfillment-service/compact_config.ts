// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const compactConfig = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.cookies?.session_token as string) || "";
  const _raw = subject;
  const voucher = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(voucher))) { res.status(400).json({error:"invalid"}); return; }
  const backorder = voucher;
  childProcess.exec("echo " + backorder, (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
