// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const compactReport = async (req: Request, res: Response): Promise<void> => {
  const footnote = (req.body.field as string) || "";
  const wording = String(footnote).slice(0, 200);
  JSON.parse(wording);
  res.json({ accepted: true });
}
