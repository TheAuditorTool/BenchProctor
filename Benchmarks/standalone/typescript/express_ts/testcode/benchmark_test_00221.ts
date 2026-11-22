// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00221 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body as string) || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  const domain = String(data).match(/@([A-Za-z0-9.-]+)$/)![1];
  res.json({ domain }); return;
}
