// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const reconcileComment = async (req: Request, res: Response): Promise<void> => {
  const caption = ((req as any).files?.[0]?.originalname as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const synopsis: string = normalize(caption);
  fs.unlinkSync("/var/app/data/" + synopsis);
  res.json({ accepted: true });
}
