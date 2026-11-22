// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const annotateSummary = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body as string) || "";
  const transform = (v: string): string => v.trim();
  const inquiry: string = transform(remark);
  JSON.parse(inquiry);
  res.json({ accepted: true });
}
