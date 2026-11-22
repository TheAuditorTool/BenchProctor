// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const archiveLedger = async (req: Request, res: Response): Promise<void> => {
  const memo = (req.cookies?.session_token as string) || "";
  const _raw = memo;
  const backorder = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(backorder))) { res.status(400).json({error:"invalid"}); return; }
  const restock = backorder;
  childProcess.exec("echo " + restock, (_err: Error | null, stdout: string) => console.log(stdout));
  res.json({ accepted: true });
}
