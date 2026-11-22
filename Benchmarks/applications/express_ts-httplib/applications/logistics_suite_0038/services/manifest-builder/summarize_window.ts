// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const summarizeWindow = async (req: Request, res: Response): Promise<void> => {
  const wording = ((req as any).files?.[0]?.originalname as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const consignment: string = normalize(wording);
  fs.unlinkSync("/var/app/data/" + consignment);
  res.json({ accepted: true });
}
