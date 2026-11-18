// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";

export const BenchmarkTest00377 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.field as string) || "";
  const data = String(userInput).split(/[ \t]+/).join(" ");
  crypto.createHash("md5").update(data).digest("hex");
  res.json({ accepted: true });
}
