// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const loadSummary = async (req: Request, res: Response): Promise<void> => {
  const remark = ((req as any).files?.[0]?.originalname as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const note: string = normalize(remark);
  fs.writeFileSync("/var/uploads/" + note, "data");
  res.json({ accepted: true });
}
