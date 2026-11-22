// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";

export const BenchmarkTest00220 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["user-agent"] as string) || "";
  const data = String(userInput).slice(0, 200);
  crypto.createHash("sha256").update(data).digest("hex");
  res.json({ accepted: true });
}
