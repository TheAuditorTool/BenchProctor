// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const BenchmarkTest00049 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (req.body.multipart_field as string) || "";
  const formData = Object.freeze({ payload: userInput });
  const data = formData.payload;
  return res.status(302).set("Location", String(data)).end();
}
