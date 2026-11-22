// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const validateSchedule = async (req: Request, res: Response): Promise<void> => {
  const headline = (req.body as string) || "";
  const transform = (v: string): string => v.trim();
  const remittance: string = transform(headline);
  JSON.parse(remittance);
  res.json({ accepted: true });
}
