// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";

export const formatPolicy = async (req: Request, res: Response): Promise<void> => {
  const phrase = (req.headers.referer as string) || "";
  const parcel = phrase != null ? phrase : '';
  const consignment = parcel.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;").replace(/'/g,"&#x27;");
  res.send("<div>" + consignment + "</div>");
}
