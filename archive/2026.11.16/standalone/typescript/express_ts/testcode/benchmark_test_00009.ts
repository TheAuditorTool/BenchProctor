// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00009 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.params.id as string) || "";
  const data = String(userInput).replace(/\u0000/g, "");
  req.session.data = String(data);
  res.json({ accepted: true });
}
