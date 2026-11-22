// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00069 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.query.id as string) || "";
  const tokens = String(userInput).split(',').filter((t) => t.length > 0);
  const data = tokens.join(' ');
  const quantity = parseInt(String(data), 10);
  const totalCents = Math.imul(quantity, 1999);
  res.json({ quantity, totalCents }); return;
}
