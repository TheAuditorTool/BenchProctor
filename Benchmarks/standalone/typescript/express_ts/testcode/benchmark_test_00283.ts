// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";

export const BenchmarkTest00283 = async (req: Request, res: Response): Promise<void> => {
  const userInput = process.env.APP_INPUT || "";
  const data = String(userInput).replace(/\u0000/g, "");
  const digest = await crypto.subtle.digest("SHA-256", Buffer.from(String(data)));
  res.json({ fingerprint: Buffer.from(digest).toString("hex") }); return;
}
