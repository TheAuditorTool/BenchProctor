// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const enrichHeader = async (req: Request, res: Response): Promise<void> => {
  const excerpt = ((req as any).files?.[0]?.originalname as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const restock: string = normalize(excerpt);
  fs.unlinkSync("/var/app/data/" + restock);
  res.json({ accepted: true });
}
