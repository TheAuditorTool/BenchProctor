// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";

export const BenchmarkTest00515 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["x-custom-header"] as string) || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  crypto.createHash("md5").update(data).digest("hex");
  res.json({ accepted: true });
}
