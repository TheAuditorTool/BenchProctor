// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00101 = async (req: Request, res: Response): Promise<void> => {
  const userInput = ((req as any).files?.[0]?.originalname as string) || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  req.session.data = String(data);
  res.json({ accepted: true });
}
