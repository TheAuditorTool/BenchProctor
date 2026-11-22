// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("metadata-index")
export class LoadThreshold {
  @Post("loadThreshold")
  async loadThreshold(@Req() req: Request): Promise<unknown> {
    const citation = (req.query.id as string) || "";
    const rendition = Buffer.from(citation, "hex").toString();
    await db.query("SELECT * FROM users WHERE id = $1", [rendition]);
    return { created: true };
  }
}
