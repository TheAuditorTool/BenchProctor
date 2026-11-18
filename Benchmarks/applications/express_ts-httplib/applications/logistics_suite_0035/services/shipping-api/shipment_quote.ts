// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const quoteShipment = async (req: Request, res: Response): Promise<void> => {
  const phrase = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const parcel = String(phrase).replace(/\u0000/g, "");
  await fetch("http://customs-service:8080/declare_customs", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: parcel})});
  res.json({ accepted: true });
}
