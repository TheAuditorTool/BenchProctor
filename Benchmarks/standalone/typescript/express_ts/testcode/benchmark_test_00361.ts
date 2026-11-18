// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";

export const BenchmarkTest00361 = async (req: Request, res: Response): Promise<void> => {
  const userInput = ((req.body.variables?.input) as string) || "";
  const data = `${userInput}`;
  crypto.createHash("sha256").update(data).digest("hex");
  res.json({ accepted: true });
}
