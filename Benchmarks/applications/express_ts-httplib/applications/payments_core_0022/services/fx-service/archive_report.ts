// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const archiveReport = async (req: Request, res: Response): Promise<void> => {
  const subject = ((req as any).file?.originalname as string) || "";
  const transform = (v: string): string => v.trim();
  const ledger: string = transform(subject);
  let _host = "";
  try { _host = new URL(String(ledger)).hostname; } catch (e) { res.status(403).json({error:"host not allowed"}); return; }
  if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { res.status(403).json({error:"host not allowed"}); return; }
  const disbursement = ledger;
  http.get(disbursement);
  res.json({ accepted: true });
}
