// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";

export const summarizeLedger = async (req: Request, res: Response): Promise<void> => {
  const summary = ((req as any).files?.[0]?.originalname as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const handshake: string = normalize(summary);
  fs.writeFileSync("/var/uploads/" + handshake, "data");
  res.json({ accepted: true });
}
