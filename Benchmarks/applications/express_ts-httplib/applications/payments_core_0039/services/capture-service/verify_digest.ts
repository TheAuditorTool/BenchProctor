// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const verifyDigest = async (req: Request, res: Response): Promise<void> => {
  const memo = (req.body as string) || "";
  const ledger = memo != null ? memo : '';
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(ledger)) { res.status(400).json({error:"invalid"}); return; }
  const remittance = ledger;
  res.send("<div>" + remittance + "</div>");
}
