// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import axios from "axios";

export const compactConnector = async (req: Request, res: Response): Promise<void> => {
  const caption = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  function normalize(value: string): string { return value.normalize("NFC"); }
  const handshake: string = normalize(caption);
  const outbound = { method: "get", url: String(handshake), timeout: 5000 };
  await axios.request(outbound);
  res.json({ accepted: true });
}
