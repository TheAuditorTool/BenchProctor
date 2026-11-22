// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const compactConfig = async (req: Request, res: Response): Promise<void> => {
  const subject = (req.body as string) || "";
  const voucher = subject != null ? subject : '';
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(voucher)) { res.status(400).json({error:"invalid"}); return; }
  const backorder = voucher;
  res.send("<div>" + backorder + "</div>");
}
