// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00595 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const data = Buffer.from(userInput, "utf-8").toString();
  res.redirect(data);
}
