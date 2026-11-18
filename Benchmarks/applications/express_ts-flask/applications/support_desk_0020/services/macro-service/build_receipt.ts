// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const buildReceipt = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.body.field as string) || "";
  const inquiry = String(phrase).slice(0, 200);
  JSON.parse(inquiry);
  res.json({ accepted: true });
}
