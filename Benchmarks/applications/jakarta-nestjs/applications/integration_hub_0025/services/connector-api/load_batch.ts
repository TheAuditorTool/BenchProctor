// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import * as path from "path";

@Controller("connector-api")
export class LoadBatch {
  @Post("loadBatch")
  async loadBatch(@Req() req: Request): Promise<unknown> {
    const footnote = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const transform = (v: string): string => v.trim();
    const handshake: string = transform(footnote);
    const resolved = path.resolve("/var/app/data", handshake);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const blurb = resolved;
    const fileContent = fs.readFileSync(blurb, "utf8");
    return fileContent;
  }
}
