// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00501 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.host as string) || "";
  const data = `${userInput}`;
  req.session.data = String(data);
  res.json({ accepted: true });
}
