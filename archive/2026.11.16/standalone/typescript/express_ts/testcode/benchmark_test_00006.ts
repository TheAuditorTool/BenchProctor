// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00006 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.referer as string) || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  JSON.parse(data);
  res.json({ accepted: true });
}
