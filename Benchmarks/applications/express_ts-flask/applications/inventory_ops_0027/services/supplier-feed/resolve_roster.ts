// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const resolveRoster = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body.field as string) || "";
  const restock = String(summary).slice(0, 200);
  JSON.parse(restock);
  res.json({ accepted: true });
}
