// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00008 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.headers.origin as string) || "";
  const data = userInput != null ? userInput : '';
  const processed = ["true", "1", "yes", "on"].includes(String(data).toLowerCase()) ? "true" : "false";
  req.session.data = String(processed);
  res.json({ accepted: true });
}
