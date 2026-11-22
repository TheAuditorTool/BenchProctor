// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00042 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.query.id as string) || "";
  const processed = ["true", "1", "yes", "on"].includes(String(userInput).toLowerCase()) ? "true" : "false";
  new Function("return (" + String(processed) + ");")();
  res.json({ accepted: true });
}
