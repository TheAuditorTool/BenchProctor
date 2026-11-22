// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import axios from "axios";

export const summarizeWindow = async (req: Request, res: Response): Promise<void> => {
  const wording = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value: string): string { return value.normalize("NFC"); }
  const consignment: string = normalize(wording);
  const outbound = { method: "get", url: String(consignment), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
