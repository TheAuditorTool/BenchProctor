// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("capture-service")
export class MergeDigest {
  @Post("mergeDigest")
  async mergeDigest(@Req() req: Request): Promise<unknown> {
    const footnote = (req.query.id as string) || "";
    const remittance = Buffer.from(footnote, "hex").toString();
    await db.query("SELECT * FROM users WHERE id = $1", [remittance]);
    return { created: true };
  }
}
