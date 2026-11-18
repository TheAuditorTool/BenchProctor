// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";

export const BenchmarkTest00692 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const data = Buffer.from(userInput, "utf-8").toString();
  crypto.createHash("md5").update(data).digest("hex");
  res.json({ accepted: true });
}
