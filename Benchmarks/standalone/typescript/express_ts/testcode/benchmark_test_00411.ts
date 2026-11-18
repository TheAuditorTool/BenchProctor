// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";

export const BenchmarkTest00411 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.query.id as string) || "";
  const data = decodeURIComponent(userInput);
  crypto.createHash("md5").update(data).digest("hex");
  res.json({ accepted: true });
}
