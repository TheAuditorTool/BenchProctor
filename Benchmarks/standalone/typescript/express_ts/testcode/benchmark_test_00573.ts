// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00573 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.query.id as string) || "";
  const transform = (v: string): string => v.trim();
  const data: string = transform(userInput);
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  eval(processed);
  res.json({ accepted: true });
}
