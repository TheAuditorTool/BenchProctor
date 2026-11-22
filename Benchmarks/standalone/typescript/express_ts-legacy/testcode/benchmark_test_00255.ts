// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import * as xpath from "xpath";
import * as xmldom from "@xmldom/xmldom";

export const BenchmarkTest00255 = async (req: Request, res: Response): Promise<void> => {
  const userInput = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const data = String(userInput).split(/[ \t]+/).join(" ");
  const usersDoc = new (xmldom.DOMParser)().parseFromString(fs.readFileSync("/var/app/data/users.xml", "utf8"), "text/xml");
  xpath.evaluate("//user[name='" + data + "']", usersDoc, null, xpath.XPathResult.ANY_TYPE, null);
  res.json({ accepted: true });
}
