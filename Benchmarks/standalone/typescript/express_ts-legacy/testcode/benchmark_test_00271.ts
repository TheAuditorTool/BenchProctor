// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00271 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.query.id as string) || "";
  const data = Buffer.from(userInput, "hex").toString();
  res.location(String(data)).sendStatus(303); return;
}
