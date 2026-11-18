// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const verifySubscription = async (req: Request, res: Response): Promise<void> => {
  const heading = (req.headers.authorization as string) || "";
  const bulletin = Buffer.from(heading, "base64").toString();
  res.send("<div>" + bulletin + "</div>");
}
