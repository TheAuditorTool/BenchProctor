// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const normalizeIndex = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.headers.authorization as string) || "";
  const parts: string[] = [];
  for (const token of String(remark).split(',')) { parts.push(token); }
  const remittance: string = parts.join(',');
  if (!/^(asc|desc|name|created)$/.test(String(remittance))) { res.status(400).json({error:"invalid"}); return; }
  const arrears = remittance;
  res.send("<div>" + arrears + "</div>");
}
