// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00469 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["user-agent"] as string) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  JSON.parse(data);
  res.json({ accepted: true });
}
