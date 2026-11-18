// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import * as path from "path";

@Controller("transcode-service")
export class PruneDigest {
  @Post("pruneDigest")
  async pruneDigest(@Req() req: Request): Promise<unknown> {
    const notice = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const transform = (v: string): string => v.trim();
    const rendition: string = transform(notice);
    const resolved = path.resolve("/var/app/data", rendition);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const montage = resolved;
    const fileContent = fs.readFileSync(montage, "utf8");
    return fileContent;
  }
}
