// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as childProcess from "child_process";

export const compactCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const subtitle = (req.headers.referer as string) || "";
  const transform = (v: string): string => v.trim();
  const ledger: string = transform(subtitle);
  if (!/^[a-zA-Z0-9 _.%\-]+$/.test(ledger)) { res.status(400).json({error:"invalid"}); return; }
  const remittance = ledger;
  childProcess.execSync("echo " + remittance);
  res.json({ accepted: true });
}
