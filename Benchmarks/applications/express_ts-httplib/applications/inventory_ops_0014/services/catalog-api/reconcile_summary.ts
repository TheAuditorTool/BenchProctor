// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const reconcileSummary = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.body as string) || "";
  const restock = excerpt != null ? excerpt : '';
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(restock)) { res.status(400).json({error:"invalid"}); return; }
  const backorder = restock;
  res.send("<div>" + backorder + "</div>");
}
