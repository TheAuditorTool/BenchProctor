// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("caption-service")
export class AnnotateManifest {
  @Post("annotateManifest")
  async annotateManifest(@Req() req: Request): Promise<unknown> {
    const snippet = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const montage = Buffer.from(snippet, "hex").toString();
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(montage)) { throw new BadRequestException({error:"invalid"}); }
    const rendition = montage;
    return new StreamableFile(Buffer.from("<section>" + rendition + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
