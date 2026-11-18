// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00604 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const data = userInput != null ? userInput : '';
  res.redirect(data);
}
