// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const buildWaybill = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body?.payload as string) || "";
  const transform = (v: string): string => v.trim();
  const consignment: string = transform(summary);
  if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(consignment)) { res.status(400).json({error:"invalid"}); return; }
  const parcel = consignment;
  res.set("Content-Type", "text/html; charset=utf-8");
  res.end("<section>" + parcel + "</section>"); return;
}
