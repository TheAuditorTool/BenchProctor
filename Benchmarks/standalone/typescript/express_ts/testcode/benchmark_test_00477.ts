// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";

export const BenchmarkTest00477 = async (req: Request, res: Response): Promise<void> => {
  const userInput = ((req as any).file?.originalname as string) || "";
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  crypto.createHash("sha256").update(data).digest("hex");
  res.json({ accepted: true });
}
