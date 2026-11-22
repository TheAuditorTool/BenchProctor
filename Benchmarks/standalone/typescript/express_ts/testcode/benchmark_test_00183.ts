// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00183 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.params.id as string) || "";
  req.session.data = String(userInput);
  res.json({ accepted: true });
}
