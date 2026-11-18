// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const loadPolicy = async (req: Request, res: Response): Promise<void> => {
  const memo = (req.query.id as string) || "";
  const parts: string[] = [];
  for (const token of String(memo).split(',')) { parts.push(token); }
  const voucher: string = parts.join(',');
  res.send("<div>" + voucher + "</div>");
}
