// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const publishConfig = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.body as string) || "";
  const transform = (v: string): string => v.trim();
  const montage: string = transform(snippet);
  JSON.parse(montage);
  res.json({ accepted: true });
}
