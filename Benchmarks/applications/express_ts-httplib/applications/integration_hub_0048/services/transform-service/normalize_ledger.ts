// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const normalizeLedger = async (req: Request, res: Response): Promise<void> => {
  const citation = ((req as any).files?.[0]?.originalname as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const handshake: string = normalize(citation);
  fs.unlinkSync("/var/app/data/" + handshake);
  res.json({ accepted: true });
}
