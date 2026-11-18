// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import * as path from "path";

@Controller("comment-service")
export class LoadDigest {
  @Post("loadDigest")
  async loadDigest(@Req() req: Request): Promise<unknown> {
    const transcript = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const transform = (v: string): string => v.trim();
    const heading: string = transform(transcript);
    const resolved = path.resolve("/var/app/data", heading);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const passage = resolved;
    const fileContent = fs.readFileSync(passage, "utf8");
    return fileContent;
  }
}
