// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";

export const collectLabel = async (req: Request, res: Response): Promise<void> => {
  const quotation = (req.cookies?.session_token as string) || "";
  const transform = (v: string): string => v.trim();
  const parcel: string = transform(quotation);
  res.send(shared.escapeHtml(parcel));
}
