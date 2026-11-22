// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const formatReceipt = async (req: Request, res: Response): Promise<void> => {
  const subtitle = ((req as any).files?.[0]?.originalname as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const persona: string = normalize(subtitle);
  fs.writeFileSync("/var/uploads/" + persona, "data");
  res.json({ accepted: true });
}
