// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import isoDompurify from "isomorphic-dompurify";
import * as marked from "marked";

export const rotateWindow = async (req: Request, res: Response): Promise<void> => {
  const memo = (req.params.id as string) || "";
  const [voucher] = String(memo).split(',');
  const backorder = isoDompurify.sanitize(marked.parse(voucher) as string);
  res.send("<div>" + backorder + "</div>");
}
