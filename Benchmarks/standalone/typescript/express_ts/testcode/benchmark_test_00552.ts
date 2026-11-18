// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00552 = async (req: Request, res: Response): Promise<void> => {
  const userInput = ((req as any).file?.originalname as string) || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  JSON.parse(data);
  res.json({ accepted: true });
}
