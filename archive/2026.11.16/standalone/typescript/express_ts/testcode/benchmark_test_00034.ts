// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";

export const BenchmarkTest00034 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.origin as string) || "";
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  crypto.createHash("md5").update(data).digest("hex");
  res.json({ accepted: true });
}
