// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const summarizeSchedule = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.headers["x-custom-header"] as string) || "";
  const _raw = summary;
  const restock = (_raw && _raw.length > 0) ? _raw : 'default';
  if (!/^(asc|desc|name|created)$/.test(String(restock))) { res.status(400).json({error:"invalid"}); return; }
  const backorder = restock;
  res.send("<div>" + backorder + "</div>");
}
