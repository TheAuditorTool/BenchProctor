// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00452 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.multipart_field as string) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  const token = String(data).slice(0, 8) + "-" + Math.floor(Math.random() * 1e12).toString(36);
  res.json({ token });
}
