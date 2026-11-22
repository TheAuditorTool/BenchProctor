// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as crypto from "crypto";

export const BenchmarkTest00045 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body?.multipart_field as string) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const digest = await crypto.subtle.digest("SHA-1", Buffer.from(String(data)));
  res.json({ fingerprint: Buffer.from(digest).toString("hex") }); return;
}
