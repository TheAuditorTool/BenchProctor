// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;

export const storeArchive = async (req: Request, res: Response): Promise<void> => {
  const wording = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const _raw = wording;
  const addendum = (_raw && _raw.length > 0) ? _raw : 'default';
  await fetch("http://document-api:8080/upload_document", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: addendum})});
  res.json({ accepted: true });
}
