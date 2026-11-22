// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const validateAddress = async (req: Request, res: Response): Promise<void> => {
  const quotation = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const transform = (v: string): string => v.trim();
  const parcel: string = transform(quotation);
  await fetch("http://carrier-gateway:8080/dispatch_carrier", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: parcel})});
  res.json({ accepted: true });
}
