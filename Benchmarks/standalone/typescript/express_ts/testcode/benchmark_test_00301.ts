// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00301 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["x-custom-header"] as string) || "";
  const [data] = String(userInput).split(',');
  JSON.parse(data);
  res.json({ accepted: true });
}
