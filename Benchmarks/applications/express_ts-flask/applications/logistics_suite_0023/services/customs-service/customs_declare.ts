// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const declareCustoms = async (req: Request, res: Response): Promise<void> => {
  const caption = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const parcel = Buffer.from(caption, "base64").toString();
  await fetch("http://rate-shopper:8000/shop_rate", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: parcel})});
  res.json({ accepted: true });
}
