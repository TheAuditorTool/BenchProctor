// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00007 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers["x-custom-header"] as string) || "";
  const payload = { get value() { return userInput; } };
  const data = payload.value;
  res.redirect(data);
}
