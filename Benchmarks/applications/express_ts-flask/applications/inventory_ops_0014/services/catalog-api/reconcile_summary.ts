// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const reconcileSummary = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (req.params.id as string) || "";
  const transform = (v: string): string => v.trim();
  const restock: string = transform(excerpt);
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(restock)) { res.status(400).json({error:"invalid"}); return; }
  const backorder = restock;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + backorder + "</section>"); return;
}
