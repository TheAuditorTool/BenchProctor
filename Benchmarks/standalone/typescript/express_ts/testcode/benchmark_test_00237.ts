// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as http from "http";

export const BenchmarkTest00237 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  http.get(data);
  res.json({ accepted: true });
}
