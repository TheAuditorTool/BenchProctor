// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00346 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.params.id as string) || "";
  let data;
  try { data = JSON.parse(userInput).value || userInput; }
  catch (e) { data = userInput; }
  return res.status(302).set("Location", String(data)).end();
}
