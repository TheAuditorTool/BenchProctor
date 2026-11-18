// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const collectHeader = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.headers.authorization as string) || "";
  const grievance = Buffer.from(summary, "base64").toString();
  res.send("<div>" + grievance + "</div>");
}
