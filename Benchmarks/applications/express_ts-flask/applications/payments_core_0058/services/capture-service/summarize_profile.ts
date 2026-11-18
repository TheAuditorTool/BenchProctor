// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const summarizeProfile = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.headers["x-custom-header"] as string) || "";
  const _raw = caption;
  const ledger = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(ledger))) { res.status(400).json({error:"invalid"}); return; }
  const remittance = ledger;
  res.send("<div>" + remittance + "</div>");
}
