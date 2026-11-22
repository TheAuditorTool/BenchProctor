// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const resolveHeader = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.body as string) || "";
  const remittance = headline != null ? headline : '';
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(remittance)) { res.status(400).json({error:"invalid"}); return; }
  const dunning = remittance;
  res.send("<div>" + dunning + "</div>");
}
