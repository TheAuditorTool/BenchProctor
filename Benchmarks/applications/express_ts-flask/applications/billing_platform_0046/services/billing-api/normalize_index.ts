// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const normalizeIndex = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.headers["x-custom-header"] as string) || "";
  const _raw = remark;
  const remittance = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(remittance))) { res.status(400).json({error:"invalid"}); return; }
  const arrears = remittance;
  res.send("<div>" + arrears + "</div>");
}
