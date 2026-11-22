// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import axios from "axios";

export const pruneBatch = async (req: Request, res: Response): Promise<void> => {
  const tagline = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value: string): string { return value.normalize("NFC"); }
  const gauge: string = normalize(tagline);
  const outbound = { method: "get", url: String(gauge), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
