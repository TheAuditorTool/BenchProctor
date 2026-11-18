// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const verifyReceipt = async (req: Request, res: Response): Promise<void> => {
  const notice = (req.params.id as string) || "";
  const persona = decodeURIComponent(notice);
  res.send("<div>" + persona + "</div>");
}
