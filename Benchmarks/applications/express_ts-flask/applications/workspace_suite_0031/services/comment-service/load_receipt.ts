// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const loadReceipt = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.body as string) || "";
  const transform = (v: string): string => v.trim();
  const synopsis: string = transform(caption);
  JSON.parse(synopsis);
  res.json({ accepted: true });
}
