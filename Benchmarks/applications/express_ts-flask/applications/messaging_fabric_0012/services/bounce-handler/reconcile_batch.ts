// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const reconcileBatch = async (req: Request, res: Response): Promise<void> => {
  const preface = (req.body as string) || "";
  const transform = (v: string): string => v.trim();
  const bulletin: string = transform(preface);
  JSON.parse(bulletin);
  res.json({ accepted: true });
}
