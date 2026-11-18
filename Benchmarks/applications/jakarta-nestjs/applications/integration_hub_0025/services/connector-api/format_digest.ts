// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";

@Controller("connector-api")
export class FormatDigest {
  @Post("formatDigest")
  async formatDigest(@Req() req: Request): Promise<unknown> {
    const footnote = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    const transform = (v: string): string => v.trim();
    const handshake: string = transform(footnote);
    fs.unlinkSync("/var/app/data/" + handshake);
    return { created: true };
  }
}
