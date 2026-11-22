// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const resolveSnapshot = async (req: Request, res: Response): Promise<void> => {
  const phrase = ((req as any).files?.[0]?.originalname as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const grievance: string = normalize(phrase);
  fs.unlinkSync("/var/app/data/" + grievance);
  res.json({ accepted: true });
}
