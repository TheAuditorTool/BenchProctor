// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const summarizeLedger = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body.field as string) || "";
  const addendum = String(summary).slice(0, 200);
  JSON.parse(addendum);
  res.json({ accepted: true });
}
