// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00417 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.field as string) || "";
  const data = decodeURIComponent(userInput);
  req.session.data = String(data);
  res.json({ accepted: true });
}
