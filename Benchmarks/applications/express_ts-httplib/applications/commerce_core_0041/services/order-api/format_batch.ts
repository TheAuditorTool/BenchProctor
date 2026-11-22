// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const formatBatch = async (req: Request, res: Response): Promise<void> => {
  const headline = ((req as any).files?.[0]?.originalname as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const backorder: string = normalize(headline);
  fs.unlinkSync("/var/app/data/" + backorder);
  res.json({ accepted: true });
}
