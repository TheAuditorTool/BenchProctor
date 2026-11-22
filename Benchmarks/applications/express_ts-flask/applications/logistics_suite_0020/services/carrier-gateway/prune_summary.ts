// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const pruneSummary = async (req: Request, res: Response): Promise<void> => {
  const transcript = (req.body as string) || "";
  const transform = (v: string): string => v.trim();
  const consignment: string = transform(transcript);
  JSON.parse(consignment);
  res.json({ accepted: true });
}
