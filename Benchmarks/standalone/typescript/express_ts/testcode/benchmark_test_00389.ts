// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00389 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.multipart_field as string) || "";
  const data = String(userInput).slice(0, 200);
  JSON.parse(data);
  res.json({ accepted: true });
}
