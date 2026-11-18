// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const annotateReceipt = async (req: Request, res: Response): Promise<void> => {
  const note = (req.headers.authorization as string) || "";
  const addendum = Buffer.from(note, "base64").toString();
  res.send("<div>" + addendum + "</div>");
}
