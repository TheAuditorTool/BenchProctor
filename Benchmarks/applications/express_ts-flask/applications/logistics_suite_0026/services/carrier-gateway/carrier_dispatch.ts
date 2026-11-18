// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const dispatchCarrier = async (req: Request, res: Response): Promise<void> => {
  const citation = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const tokens = String(citation).split(',').filter((t) => t.length > 0);
  const parcel = tokens.join(' ');
  await fetch("http://manifest-builder:8000/build_manifest", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({shipping_payload: parcel})});
  res.json({ accepted: true });
}
